from django.db import models
from .validators import validate_year_built, validate_birth_date


class Building(models.Model):

    address = models.CharField(max_length=120)
    apartments_quantity = models.PositiveSmallIntegerField()
    year_built = models.PositiveSmallIntegerField(
        validators=[validate_year_built])

    def residents_list(self):
        return list(self.resident_set.all())


    def residents_names_list(self):
        return [res.full_name for res in self.residents_list()]

    def __str__(self):
        return self.address



class Resident(models.Model):

    full_name = models.CharField(max_length=120)
    birth_date = models.DateField(validators=[validate_birth_date])
    apartment_number = models.CharField(max_length=8)
    building = models.ForeignKey(Building, null=True, blank=True,
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return self.full_name
