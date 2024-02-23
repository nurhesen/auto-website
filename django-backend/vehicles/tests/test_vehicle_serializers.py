from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from ..models import Vehicle, VehicleImages
from ..serializers import VehicleImageSerializer, VehicleListSerializer
from brands.models import VehicleModel, VehicleBrand
import logging



def create_vehicle(title='Test Vehicle', color='Black', condition=1, fuel=1, price=10000,
                    currency=1, brand_model=None, vehicle_type=1, classification=1, km_traveled=50000.0,
                    year=2019):
    
    vehicle_brand = VehicleBrand.objects.create(name='Test Brand')
    vehicle_model = VehicleModel.objects.create(name='Test Model', brand=vehicle_brand)

    vehicle =  Vehicle.objects.create(
        title=title,
        color=color,
        condition=condition,
        fuel=fuel,
        price=price,
        currency=currency,
        brand_model=vehicle_model,
        vehicle_type=vehicle_type,
        classification=classification,
        km_traveled=km_traveled,
        year=year
    )

    VehicleImages.objects.create(image='/test-image.jpg', post=vehicle)

    return vehicle



class VehicleImageSerializerTest(TestCase):
    def setUp(self):
        self.vehicle=create_vehicle()
        self.images=self.vehicle.images

    def test_valid_data(self):
        serializer = VehicleImageSerializer(self.images.all(), many=True)
        self.assertEqual(len(serializer.data), 1)


    def test_missing_image(self):
        self.images.first().delete()
        serializer = VehicleImageSerializer(self.images.all(), many=True)
        self.assertEqual(len(serializer.data), 0)


class VehicleListSerializerTest(TestCase):
    def setUp(self):
        self.init_data = {
            'title': 'Test Vehicle',
            'color': 'Red',
            'condition': 1,
            'fuel': 1,
            'price': 10000.0,
            'currency': 1,
            'vehicle_type': 1,
            'classification': 1,
            'km_traveled': 50000.0,
            'year': 2020,
        }

        self.expected_data =  {'id': 13, 
                                'condition': 'new', 
                                'fuel': 'Gasoline', 
                                'currency': 'EURO', 
                                'vehicle_type': 'Car', 
                                'classification': 'Modern', 
                                'brand_model': 'Test Brand Test Model', 
                                'image': '/test-image.jpg',
                                'title': 'Test Vehicle', 
                                'color': 'Red', 
                                'price': 10000.0, 
                                'km_traveled': 50000.0, 
                                'year': 2020}
        
        self.vehicle = create_vehicle(**self.init_data)
        self.vehicle_image = self.vehicle.images.all()
        

    def test_serializer_output(self):
        serializer = VehicleListSerializer(instance=self.vehicle)
        self.assertEqual(serializer.data, self.expected_data)

