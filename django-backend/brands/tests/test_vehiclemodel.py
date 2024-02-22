from django.test import TestCase
from brands.models import VehicleBrand, VehicleModel


class VehicleModelTestCase(TestCase):
    def setUp(self):
        # Create a VehicleBrand object
        self.brand = VehicleBrand.objects.create(name='Test Brand')

    def test_vehicle_model_creation(self):
        # Create a VehicleModel object
        model = VehicleModel.objects.create(name='Test Model', brand=self.brand)

        # Retrieve the model from the database
        saved_model = VehicleModel.objects.get(name='Test Model')

        # Check that the model was created successfully
        self.assertEqual(model, saved_model)

    def test_vehicle_model_full_name(self):
        # Create a VehicleModel object
        model = VehicleModel.objects.create(name='Test Model', brand=self.brand)

        # Check the full name of the model
        self.assertEqual(model.full_name(), 'Test Brand Test Model')
