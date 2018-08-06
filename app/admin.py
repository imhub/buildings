from django.contrib import admin
from .models import Building, Resident


class ResidentInline(admin.TabularInline):
    model = Resident

class BuildingAdmin(admin.ModelAdmin):
    list_display = ['address', 'apartments_quantity', 'year_built',
                    'residents_list']
    inlines = [ResidentInline, ]


admin.site.register(Building, BuildingAdmin)
admin.site.register(Resident)