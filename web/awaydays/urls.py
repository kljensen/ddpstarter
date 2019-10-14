from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('locations/', views.location_list, name='location_list'),
    path('locations/view/<int:pk>', views.location_detail, name='location_view'),
    path('locations/new', views.location_create, name='location_new'),
    path('locations/edit/<int:pk>',
         views.location_update, name='location_edit'),
    path('locations/delete/<int:pk>',
         views.location_delete, name='location_delete'),
]
