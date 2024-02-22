
from django.contrib import admin
from django.urls import path

from vehicles.views import VehiclesListView, VehicleDetailView, VehicleBrandView

urlpatterns = [
    path('brands/', VehicleBrandView.as_view()),
    path('', VehiclesListView.as_view(), name='vehicles-list'),
    path('<int:id>/', VehicleDetailView.as_view()),
]
