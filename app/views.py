from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Building, Resident


def homepage(request):
    return render(request, 'homepage.html')


class BuildingList(ListView):

    model = Building

    def get_queryset(self):
        buildings = Building.objects.all()
        order = self.request.GET.get('order_by', '')
        if order in ('address', 'apartments_quantity', 'year_built'):
            buildings = Building.objects.order_by(order)
            if self.request.GET.get('reverse', '') == '1':
                buildings = buildings.reverse()
        return buildings

class ResidentList(ListView):

    model = Resident

    def get_queryset(self):
        residents = Resident.objects.all()
        order = self.request.GET.get('order_by', '')
        if order in ('full_name', 'birth_date', 'apartment_number'):
            residents = residents.order_by(order)
            if self.request.GET.get('reverse', '') == '1':
                residents = residents.reverse()
        return residents


class BuildingResidentsList(ListView):

    model = Resident

    def get_queryset(self):
        self.building = get_object_or_404(Building,
                                          pk=self.kwargs['building_pk'])
        building_residents = Resident.objects.filter(building=self.building)
        order = self.request.GET.get('order_by', '')
        if order in ('full_name', 'birth_date', 'apartment_number'):
            building_residents = building_residents.order_by(order)
            if self.request.GET.get('reverse', '') == '1':
                building_residents = building_residents.reverse()
        return building_residents
