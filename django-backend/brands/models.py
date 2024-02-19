from django.db import models


class VehicleBrand(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name


class VehicleModel(models.Model):
    name=models.CharField(max_length=250)
    brand=models.ForeignKey(VehicleBrand, on_delete=models.CASCADE, related_name='vehicle_models')

    def full_name(self):
        return self.brand.name + " " + self.name

    def __str__(self):
        return self.brand.name + " " +self.name
