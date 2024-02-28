from django.test import TestCase
from vehicles.models import Vehicle, VehicleImages
from brands.models import VehicleBrand, VehicleModel


class VehicleImagesTestCase(TestCase):
    def setUp(self):
        # Create necessary objects for testing
        self.brand = VehicleBrand.objects.create(name='Test Brand')
        self.vehicle_model = VehicleModel.objects.create(
            name='Test Model',
            brand=self.brand
            )
        self.vehicle = Vehicle.objects.create(
            title='Test Vehicle',
            color='Black',
            condition=1,  # 1 for 'new'
            fuel=1,  # 1 for 'Gasoline'
            price=10000.0,
            currency=1,  # 1 for 'EURO'
            brand_model=self.vehicle_model,
            vehicle_type=1,  # 1 for 'Car'
            classification=1,  # 1 for 'Modern'
            km_traveled=50000.0,
            year=2022
        )

    def test_vehicle_image_creation(self):
        # Create a VehicleImage object
        VehicleImages.objects.create(
            image='/test-image.jpg',
            post=self.vehicle
        )

        # Assert that the image was created successfully
        self.assertEqual(VehicleImages.objects.count(), 1)
