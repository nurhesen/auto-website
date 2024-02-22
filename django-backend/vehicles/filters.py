import django_filters
from .models import Vehicle

class VehicleFilter(django_filters.FilterSet):
    min_year = django_filters.NumberFilter(field_name='year', lookup_expr='gte')
    max_year = django_filters.NumberFilter(field_name='year', lookup_expr='lte')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    min_km_traveled = django_filters.NumberFilter(field_name='km_traveled', lookup_expr='gte')
    max_km_traveled = django_filters.NumberFilter(field_name='km_traveled', lookup_expr='lte')

    class Meta:
        model = Vehicle
        fields = ['min_year', 'max_year', 'min_price', 'max_price', 'fuel', 'min_km_traveled', 'max_km_traveled', 'color', 'condition', 'classification', 'vehicle_type']
