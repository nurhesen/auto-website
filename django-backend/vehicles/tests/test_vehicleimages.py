from django.test import TestCase
from vehicles.models import Vehicle, VehicleImages
from brands.models import VehicleBrand, VehicleModel


class VehicleImagesTestCase(TestCase):
    def setUp(self):
        # Create necessary objects for testing
        self.brand = VehicleBrand.objects.create(name='Test Brand')
        self.vehicle_model = VehicleModel.objects.create(name='Test Model', brand=self.brand)
        self.vehicle = Vehicle.objects.create(
            title='Test Vehicle',
            color='Black',
            condition=1,  # Use valid condition value (1 for 'new')
            fuel=1,  # Use valid fuel value (1 for 'Gasoline')
            price=10000.0,
            currency=1,  # Use valid currency value (1 for 'EURO')
            brand_model=self.vehicle_model,
            vehicle_type=1,  # Use valid vehicle_type value (1 for 'Car')
            classification=1,  # Use valid classification value (1 for 'Modern')
            km_traveled=50000.0,
            year=2022
        )

    def test_vehicle_image_creation(self):
        # Create a VehicleImage object
        image = VehicleImages.objects.create(
            image='/test-image.jpg',
            post=self.vehicle
        )

        # Assert that the image was created successfully
        self.assertEqual(VehicleImages.objects.count(), 1)
