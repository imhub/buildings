from django.urls import path
from .views import BuildingList, BuildingResidentsList

urlpatterns = [path('buildings/',
                    BuildingList.as_view(template_name='buildings_list.html'),
                    name='buildings'),
               path('residents/<building_pk>/', BuildingResidentsList.as_view(
                   template_name='residents_list.html'), name='residents')]
