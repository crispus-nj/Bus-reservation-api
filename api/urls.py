from django.urls import path
from . import views
urlpatterns = [
    path('find-bus', views.find_bus, name='find_bus'),
    path('reservation', views.send_reservation)
]
