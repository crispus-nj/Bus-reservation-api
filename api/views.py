from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Bus, Passenger, Reservationn
from .serializers import BusSerializers, PassengerSerializers, ReservationSerializers
# Create your views here.


@api_view(['POST'])
def find_bus(request):
    bus = Bus.objects.filter(departure_city = request.data['departure_city'], arrival_city=request.data['arrival_city'])
    serializer = BusSerializers(bus, many=True)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def send_reservation(request):
    bus = Bus.objects.get(id = request.data['id'])

    passenger = Passenger()
    passenger.username = request.data['username']
    passenger.email = request.data['email']
    passenger.phone_number = request.data['phone_number']
    passenger.save()

    reservation = Reservationn()
    reservation.bus = bus
    reservation.passenger = passenger
    reservation.save()

    return Response(reservation.data,status=status.HTTP_201_CREATED)


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializers
    permission_classes = [IsAuthenticated]

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializers

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservationn.objects.all()
    serializer_class = ReservationSerializers

