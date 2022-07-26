from .models import Vehicle, VehicleImages
from rest_framework import serializers






class VehicleImageSerializer(serializers.ModelSerializer):

    class Meta:
        model=VehicleImages
        fields=('image',)


class VehicleListSerializer(serializers.ModelSerializer):
    condition = serializers.CharField(source='get_condition_display')
    fuel = serializers.CharField(source='get_fuel_display')
    currency = serializers.CharField(source='get_currency_display')
    vehicle_type = serializers.CharField(source='get_vehicle_type_display')
    classification = serializers.CharField(source='get_classification_display')
    brand_model = serializers.SerializerMethodField('get_brand_model')
    image = serializers.SerializerMethodField('get_images')

    def get_brand_model(self, obj):
        return obj.brand_model.full_name()
    def get_images(self, obj):
        model=obj.images.all().first()

        return model.image.url
    class Meta:
        model=Vehicle
        fields='__all__'


class VehicleSerializer(serializers.ModelSerializer):
    condition = serializers.CharField(source='get_condition_display')
    fuel = serializers.CharField(source='get_fuel_display')
    currency = serializers.CharField(source='get_currency_display')
    vehicle_type = serializers.CharField(source='get_vehicle_type_display')
    classification = serializers.CharField(source='get_classification_display')
    brand_model = serializers.SerializerMethodField('get_brand_model')
    images = serializers.SerializerMethodField('get_images')

    def get_brand_model(self, obj):
        return obj.brand_model.full_name()
    def get_images(self, obj):
        model=obj.images.all()
        serializer = VehicleImageSerializer(model, many=True)
        return serializer.data
    class Meta:
        model=Vehicle
        fields='__all__'

