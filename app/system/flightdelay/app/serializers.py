from rest_framework import serializers
from .models import *

class AirportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airports
        fields = (
            'airport', 'airport_name',
        )

class CarriersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carriers
        fields = (
            'carrier', 'carrier_name',
        )

class FlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = (
            'id', 'year', 'month', 'carrier', 'airport', 'arr_flights', 'arr_del15', 'carrier_ct', 'weather_ct', 'nas_ct', 'security_ct', 'late_aircraft_ct', 'arr_cancelled', 'arr_diverted', 'arr_delay', 'carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay')


