from django.db import models
from brands.models import VehicleModel




class Vehicle(models.Model):
    Conditions=(
        (1, ("new")),
        (2, ("used")),
    )
    Currencies=(
        (1, ("EURO")),
        (2, ("USD")),
    )
    Vehicle_types = (
        (1, ("Car")),
        (2, ("Motorcycle")),
    )
    Classifications = (
        (1, ("Modern")),
        (2, ("Classic")),
        (3, ("Antique")),
        (4, ("Vintage")),
    )
    Fuels = (
        (1, ("Gasoline")),
        (2, ("Diesel")),
        (3, ("Gas")),
        (4, ("Electro")),
        (4, ("Hybrid")),
    )
    title=models.CharField(max_length=250)
    color=models.CharField(max_length=250)
    condition = models.IntegerField(choices=Conditions, default="new")
    fuel = models.IntegerField(choices=Fuels, default="Gasoline")
    price = models.FloatField()
    currency = models.IntegerField(choices=Currencies, default="EURO")
    brand_model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE, related_name='vehicles')
    vehicle_type = models.IntegerField(choices=Vehicle_types, default="Car")
    classification = models.IntegerField(choices=Classifications, default="Modern")
    km_traveled = models.FloatField()
    year = models.IntegerField()

    

    def __str__(self):
        return self.title

class VehicleImages(models.Model):
    image=models.ImageField(upload_to ='media/vehicles/%Y/%m/%d/')
    post=models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='images')


    def __str__(self):
        return str(self.image).split('/')[-1]