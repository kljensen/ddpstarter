from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ---- Locations
    path('locations/', views.location_list, name='location_list'),
    path('locations/view/<int:pk>', views.location_detail, name='location_view'),
    path('locations/new', views.location_create, name='location_create'),
    path('locations/edit/<int:pk>',
         views.location_update, name='location_edit'),
    path('locations/delete/<int:pk>',
         views.location_delete, name='location_delete'),
    # ----- AwayPlans
    path('awayplans/', views.awayplan_list, name='awayplan_list'),
    path('awayplans/view/<int:pk>', views.awayplan_detail, name='awayplan_view'),
    path('awayplans/new', views.awayplan_create, name='awayplan_create'),
    path('awayplans/edit/<int:pk>',
         views.awayplan_update, name='awayplan_edit'),
    path('awayplans/delete/<int:pk>',
         views.awayplan_delete, name='awayplan_delete'),
]
