from django.urls import path
from .views import BuildingList, ResidentList, BuildingResidentsList

urlpatterns = [path('buildings/',
                    BuildingList.as_view(template_name='buildings_list.html'),
                    name='buildings'),
               path('residents/', ResidentList.as_view(
                   template_name='residents_list.html'), name='residents'),
               path('residents/<building_pk>/', BuildingResidentsList.as_view(
                   template_name='building_residents.html'),
                    name='building_residents')]
