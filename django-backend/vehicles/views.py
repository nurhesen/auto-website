from rest_framework.views import APIView
from brands.models import VehicleBrand, VehicleModel
from auto.utils import CustomFilter
from rest_framework import status
from vehicles.serializers import VehicleListSerializer, VehicleSerializer
from .models import Vehicle
from rest_framework.response import Response




class VehicleBrandView(APIView):
    def get(self, request,  format=None):
        model=VehicleBrand.objects.all()
        return Response({'brands':[m.name for m in model]})




class VehicleView(APIView):
    def get(self, request, id, format=None):
        model=Vehicle.objects.filter(id=id).first()
        if not model:
            return Response({'message':'No data'}, status=status.HTTP_404_NOT_FOUND)
        serializer=VehicleSerializer(model)
        return Response(serializer.data)




class VehiclesListView(APIView):
    def get(self, request, format=None):
        
        query={
            'brand':request.query_params.get('brand'),
            'model':request.query_params.get('model'),
        }
        
        if query['brand']:
            brand=VehicleBrand.objects.filter(name=query['brand'])
            if query['model']:
                model=VehicleModel.objects.filter(brand__in=brand, name=query['model'])
            else:
                model=VehicleModel.objects.filter(brand__in=brand)
        else:
            model=VehicleModel.objects.all()

        veh=Vehicle.objects.filter(brand_model__in=model)
        fields=['min_year','max_year','min_price','max_price','fuel','max_km_traveled', 'min_km_traveled','color','condition','classification','vehicle_type']
        
        vehicle=CustomFilter(veh, request, fields).filter()

        serializer=VehicleListSerializer(vehicle, many=True)
        return Response(serializer.data)

