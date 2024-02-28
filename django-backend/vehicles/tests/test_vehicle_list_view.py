from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from vehicles.models import Vehicle, VehicleImages
from brands.models import VehicleBrand, VehicleModel


class VehiclesListViewTest(APITestCase):
    def create_vehicle(
            self,
            title='Test Vehicle',
            color='Black',
            condition=1,
            fuel=1,
            price=10000,
            currency=1,
            brand_model=None,
            vehicle_type=1,
            classification=1,
            km_traveled=50000.0,
            year=2019
            ):
        vehicle = Vehicle.objects.create(
            title=title,
            color=color,
            condition=condition,
            fuel=fuel,
            price=price,
            currency=currency,
            brand_model=brand_model,
            vehicle_type=vehicle_type,
            classification=classification,
            km_traveled=km_traveled,
            year=year
        )

        VehicleImages.objects.create(image='/test-image.jpg', post=vehicle)

        return vehicle

    def setUp(self):
        # Create some test vehicles
        vehicle_brand = VehicleBrand.objects.create(name='Test Brand')
        vehicle_model = VehicleModel.objects.create(
            name='Test Model',
            brand=vehicle_brand
            )

        self.vehicle1 = self.create_vehicle(brand_model=vehicle_model)
        self.vehicle2 = self.create_vehicle(
            condition=2,
            price=18000,
            currency=2,
            brand_model=vehicle_model
            )
        self.vehicle3 = self.create_vehicle(
            condition=1,
            price=18000,
            currency=1,
            brand_model=vehicle_model
            )

    def test_filter_vehicles_max_min(self):
        url = reverse('vehicles-list')
        data = {'min_year': 2018,
                'max_year': 2020,
                'min_price': 15000,
                'max_price': 20000
                }
        response = self.client.get(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_vehicles_exact(self):
        url = reverse('vehicles-list')
        data = {'condition': 2, 'currency': 1}
        response = self.client.get(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_vehicles_empty(self):
        url = reverse('vehicles-list')
        data = {}
        response = self.client.get(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
