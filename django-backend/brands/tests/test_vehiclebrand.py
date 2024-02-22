from django.test import TestCase
from brands.models import VehicleBrand

class VehicleBrandTestCase(TestCase):
    def test_vehicle_brand_creation(self):
        # Create a VehicleBrand object
        brand = VehicleBrand.objects.create(name='Test Brand')

        # Retrieve the brand from the database
        saved_brand = VehicleBrand.objects.get(name='Test Brand')

        # Check that the brand was created successfully
        self.assertEqual(brand, saved_brand)

