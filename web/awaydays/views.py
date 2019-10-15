from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm, ValidationError
from .models import Location, AwayPlan
from bootstrap_datepicker_plus import DateTimePickerInput
from django.db.utils import DataError
from django.contrib.auth.decorators import login_required


def index(request):
    context_data = {
        "session": request.session
    }
    return render(request, 'index.html', context_data)

# See https://rayed.com/posts/2018/05/django-crud-create-retrieve-update-delete/
# for simple CRUD instructions using the generic views in Django.


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ('address1', 'address2', 'city', 'zip_code', 'notes')


@login_required
def location_list(request, template_name='awaydays/location/list.html'):
    location = Location.objects.filter(user=request.user)
    data = {}
    data['object_list'] = location
    return render(request, template_name, data)


@login_required
def location_detail(request, pk, template_name='awaydays/location/detail.html'):
    location = get_object_or_404(Location, user=request.user, pk=pk)
    return render(request, template_name, {'object': location})


@login_required
def location_create(request, template_name='awaydays/location/form.html'):
    form = LocationForm(request.POST or None)
    form.user = request.user
    if form.is_valid():
        form.save()
        return redirect('location_list')
    return render(request, template_name, {'form': form})


@login_required
def location_update(request, pk, template_name='awaydays/location/form.html'):
    location = get_object_or_404(Location, user=request.user, pk=pk)
    form = LocationForm(request.POST or None, instance=location)
    if form.is_valid():
        form.save()
        return redirect('location_list')
    return render(request, template_name, {'form': form})


@login_required
def location_delete(request, pk, template_name='awaydays/location/confirm_delete.html'):
    location = get_object_or_404(Location, user=request.user, pk=pk)
    if request.method == 'POST':
        location.delete()
        return redirect('location_list')
    return render(request, template_name, {'object': location})


# ----- CRUD for AwayPlan reservations


class AwayPlanForm(ModelForm):
    class Meta:
        model = AwayPlan
        fields = '__all__'
        widgets = {
            'start_date': DateTimePickerInput(),
            'end_date': DateTimePickerInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if end_date <= start_date:
            raise ValidationError(
                "The end date must be after the start date for your plan"
            )


@login_required
def awayplan_list(request, template_name='awaydays/awayplan/list.html'):
    awayplan = AwayPlan.objects.filter(location__user=request.user)
    data = {}
    data['object_list'] = awayplan
    return render(request, template_name, data)


@login_required
def awayplan_detail(request, pk, template_name='awaydays/awayplan/detail.html'):
    awayplan = get_object_or_404(AwayPlan, pk=pk)
    return render(request, template_name, {'object': awayplan})


def awayplan_save(success_redirect, request, failure_template_name, form):
    """ Save an away plan. If we succeed, redirect. Otherwise save the form.

    Arguments:
        success_redirect {string} -- route name to which we should redirect if successful
        request {request} -- Request object
        failure_template_name {string} -- template name we should render upon failure
        form {form} -- form into which we should stick validation exceptions
    """
    if form.is_valid():
        try:
            form.save()
            return redirect(success_redirect)
        except (DataError,) as e:
            form.add_error(None, e)

    return render(request, failure_template_name, {'form': form})


@login_required
def awayplan_create(request, template_name='awaydays/awayplan/form.html'):
    form = AwayPlanForm(request.POST or None)
    return awayplan_save('awayplan_list', request, template_name, form)


@login_required
def awayplan_update(request, pk, template_name='awaydays/awayplan/form.html'):
    awayplan = get_object_or_404(AwayPlan, location__user=request.user, pk=pk)
    form = AwayPlanForm(request.POST or None, instance=awayplan)
    return awayplan_save('awayplan_list', request, template_name, form)


@login_required
def awayplan_delete(request, pk, template_name='awaydays/awayplan/confirm_delete.html'):
    awayplan = get_object_or_404(AwayPlan, location__user=request.user, pk=pk)
    if request.method == 'POST':
        awayplan.delete()
        return redirect('awayplan_list')
    return render(request, template_name, {'object': awayplan})
