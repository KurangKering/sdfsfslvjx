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

class DatasetRawSerializer(serializers.ModelSerializer):
    carrier = serializers.CharField(source='carrier.carrier', read_only=True)
    carrier_name = serializers.CharField(source='carrier.carrier_name', read_only=True)
    airport = serializers.CharField(source='airport.airport', read_only=True)
    airport_name = serializers.CharField(source='airport.airport_name', read_only=True)

    class Meta:
        model = DatasetRaw
        fields = '__all__'



class DatasetCleanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetClean
        fields = '__all__'
