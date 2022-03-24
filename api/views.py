from django.shortcuts import render
from rest_framework import viewsets
from .models import Bus, Passenger, Reservationn
from .serializers import BusSerializers, PassengerSerializers, ReservationSerializers
# Create your views here.

class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializers

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializers

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservationn.objects.all()
    serializer_class = ReservationSerializers

