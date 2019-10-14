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


def location_list(request, template_name='awaydays/location_list.html'):
    location = Location.objects.all()
    data = {}
    data['object_list'] = location
    return render(request, template_name, data)


def location_detail(request, pk, template_name='awaydays/location_detail.html'):
    location = get_object_or_404(Location, pk=pk)
    return render(request, template_name, {'object': location})


def location_create(request, template_name='awaydays/location_form.html'):
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('location_list')
    return render(request, template_name, {'form': form})


def location_update(request, pk, template_name='awaydays/location_form.html'):
    location = get_object_or_404(Location, pk=pk)
    form = LocationForm(request.POST or None, instance=location)
    if form.is_valid():
        form.save()
        return redirect('location_list')
    return render(request, template_name, {'form': form})


def location_delete(request, pk, template_name='awaydays/location_confirm_delete.html'):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        location.delete()
        return redirect('location_list')
    return render(request, template_name, {'object': location})
