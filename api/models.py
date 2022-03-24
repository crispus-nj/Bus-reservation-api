from django.db import models

# Create your models here.
class Bus(models.Model):
    bus_number = models.CharField(max_length=10)
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    estimated_time_of_departure = models.TimeField()

    def __str__(self):
        return self.bus_number

class Passenger(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.username

class Reservationn(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return self.bus.bus_number