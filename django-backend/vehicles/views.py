from rest_framework.views import APIView
from brands.models import VehicleBrand
from rest_framework import status
from vehicles.serializers import VehicleListSerializer, VehicleSerializer
from .models import Vehicle
from rest_framework.response import Response
from rest_framework import generics
from .filters import VehicleFilter


class VehicleBrandView(APIView):
    def get(self, request,  format=None):
        model = VehicleBrand.objects.all()
        return Response({'brands': [m.name for m in model]})


class VehicleDetailView(APIView):
    def get(self, request, id, format=None):
        model = Vehicle.objects.filter(id=id).first()
        if not model:
            return Response(
                {'message': 'No data'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = VehicleSerializer(model)
        return Response(serializer.data)


class VehiclesListView(generics.ListAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleListSerializer
    filterset_class = VehicleFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
