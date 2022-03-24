from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Bus, Passenger, Reservationn
from .serializers import BusSerializers, PassengerSerializers, ReservationSerializers
# Create your views here.


@api_view(['POST'])
def find_bus(request):
    print(request.data)
    bus = Bus.objects.filter(departure_city = request.data['departure_city'], arrival_city=request.data['arrival_city'])
    serializer = BusSerializers(bus, many=True)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializers

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializers

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservationn.objects.all()
    serializer_class = ReservationSerializers

