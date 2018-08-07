from django.test import TestCase
from .models import Building, Resident


class ModelsTest(TestCase):

    def create_building(self, address, apartments_quantity, year_built):
        return Building.objects.create(address=address,
                                       apartment_quantity=apartments_quantity,
                                       year_built=year_built)

    def create_resident(self, full_name='Tom Waits', birth_date=1949,
                        apartment_number='A1',
                        building=create_building(self,
                                                 address="1, Khreschatyk Str",
                                                 apartments_quantity=15,
                                                 year_built=1900)):


    def test_building_creation(self):
        b = self.create_building(self, address="1, Khreschatyk Str",
                                 apartments_quantity=15, year_built=1900)
        self.assertTrue(isinstance(b, Building))
        self.assertEqual(b.__str__(), b.address)


class Building(models.Model):

    address = models.CharField(max_length=120)
    apartments_quantity = models.PositiveSmallIntegerField()
    year_built = models.PositiveSmallIntegerField()

    def residents_list(self):
        return list(self.resident_set.all())


    def residents_names_list(self):
        return [res.full_name for res in self.residents_list()]

    def __str__(self):
        return self.address

    class Resident(models.Model):
        full_name = models.CharField(max_length=120)
        birth_date = models.DateField()
        apartment_number = models.CharField(max_length=8)
        building = models.ForeignKey(Building, null=True, blank=True,
                                     on_delete=models.SET_NULL)

        def __str__(self):
            return self.full_name