from rest_framework import serializers
from .models import Bus, Passenger, Reservationn

class BusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class PassengerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservationn
        fields = '__all__'