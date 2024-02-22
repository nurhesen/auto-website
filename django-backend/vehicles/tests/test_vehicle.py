from django.test import TestCase
from vehicles.models import Vehicle
from brands.models import VehicleBrand, VehicleModel

class VehicleModelTestCase(TestCase):
    def setUp(self):
        # Create a VehicleBrand object
        self.brand = VehicleBrand.objects.create(name='Test Brand')

        # Create a VehicleModel object associated with the brand
        self.vehicle_model = VehicleModel.objects.create(name='Test Model', brand=self.brand)

    def test_vehicle_creation(self):
        # Create a vehicle object with valid values
        vehicle = Vehicle.objects.create(
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

        # Assert that the vehicle was created successfully
        self.assertEqual(Vehicle.objects.count(), 1)
