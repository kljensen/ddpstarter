from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import Location, AwayPlan


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
        fields = '__all__'


def location_list(request, template_name='awaydays/location/list.html'):
    location = Location.objects.all()
    data = {}
    data['object_list'] = location
    return render(request, template_name, data)


def location_detail(request, pk, template_name='awaydays/location/detail.html'):
    location = get_object_or_404(Location, pk=pk)
    return render(request, template_name, {'object': location})


def location_create(request, template_name='awaydays/location/form.html'):
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('location_list')
    return render(request, template_name, {'form': form})


def location_update(request, pk, template_name='awaydays/location/form.html'):
    location = get_object_or_404(Location, pk=pk)
    form = LocationForm(request.POST or None, instance=location)
    if form.is_valid():
        form.save()
        return redirect('location_list')
    return render(request, template_name, {'form': form})


def location_delete(request, pk, template_name='awaydays/location/confirm_delete.html'):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        location.delete()
        return redirect('location_list')
    return render(request, template_name, {'object': location})


# ----- CRUD for AwayPlan reservations


class AwayPlanForm(ModelForm):
    class Meta:
        model = AwayPlan
        fields = '__all__'


def awayplan_list(request, template_name='awaydays/awayplan/list.html'):
    awayplan = AwayPlan.objects.all()
    data = {}
    data['object_list'] = awayplan
    return render(request, template_name, data)


def awayplan_detail(request, pk, template_name='awaydays/awayplan/detail.html'):
    awayplan = get_object_or_404(AwayPlan, pk=pk)
    return render(request, template_name, {'object': awayplan})


def awayplan_create(request, template_name='awaydays/awayplan/form.html'):
    form = AwayPlanForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('awayplan_list')
    return render(request, template_name, {'form': form})


def awayplan_update(request, pk, template_name='awaydays/awayplan/form.html'):
    awayplan = get_object_or_404(AwayPlan, pk=pk)
    form = AwayPlanForm(request.POST or None, instance=awayplan)
    if form.is_valid():
        form.save()
        return redirect('awayplan_list')
    return render(request, template_name, {'form': form})


def awayplan_delete(request, pk, template_name='awaydays/awayplan/confirm_delete.html'):
    awayplan = get_object_or_404(AwayPlan, pk=pk)
    if request.method == 'POST':
        awayplan.delete()
        return redirect('awayplan_list')
    return render(request, template_name, {'object': awayplan})
