from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import filters
from django.db.models import Q
import pandas as pd

# Create your views here.

def airports(request):
	return render(request, 'airports.html')

def carriers(request):
	return render(request, 'carriers.html')

def dataset_raw(request):
	return render(request, 'dataset-raw.html')

def dataset_clean(request):
	# process cleaning dataset and showing the output

    df = DatasetRaw.objects.all()
    df1 = df.to_dataframe()
    df1 = df[df.isna().any(axis=1)]


    data = [DatasetNull(
        id = models.AutoField(primary_key=True)
        year = models.IntegerField(null=True, blank=True)
        month = models.IntegerField(null=True, blank=True)
        carrier = models.TextField(null=True, blank=True)
        airport = models.TextField(null=True, blank=True)
        arr_flights = models.FloatField(null=True, blank=True)
        arr_del15 = models.FloatField(null=True, blank=True)
        carrier_ct = models.FloatField(null=True, blank=True)
        weather_ct = models.FloatField(null=True, blank=True)
        nas_ct = models.FloatField(null=True, blank=True)
        security_ct = models.FloatField(null=True, blank=True)
        late_aircraft_ct = models.FloatField(null=True, blank=True)
        arr_cancelled = models.FloatField(null=True, blank=True)
        arr_diverted = models.FloatField(null=True, blank=True)
        arr_delay = models.FloatField(null=True, blank=True)
        carrier_delay = models.FloatField(null=True, blank=True)
        weather_delay = models.FloatField(null=True, blank=True)
        nas_delay = models.FloatField(null=True, blank=True)
        security_delay = models.FloatField(null=True, blank=True)
        late_aircraft_delay = models.FloatField(null=True, blank=True)
          
          age=dataset.age,
                                                sex=dataset.sex,
                                                steroid=dataset.steroid,
                                                antivirals=dataset.antivirals,
                                                fatigue=dataset.fatigue,
                                                malaise=dataset.malaise,
                                                anorexia=dataset.anorexia,
                                                liver_big=dataset.liver_big,
                                                liver_firm=dataset.liver_firm,
                                                spleen_palpable=dataset.spleen_palpable,
                                                spiders=dataset.spiders,
                                                ascites=dataset.ascites,
                                                varices=dataset.varices,
                                                bilirubin=dataset.bilirubin,
                                                alk_posphate=dataset.alk_posphate,
                                                sgot=dataset.sgot,
                                                albumin=dataset.albumin,
                                                protime=dataset.protime,
                                                histology=dataset.histology,
                                                kelas=dataset.kelas, ) for dataset in df1.itertuples()]

    DatasetRaw.objects.bulk_create()
    pass
    return render(request, 'dataset-clean.html')

def preprocessing(request):
	return render(request, 'preprocessing.html')

def cleaning(request):
	return render(request, 'cleaning.html')

def classifier(request):
	return render(request, 'classifier.html')

def prediction(request):
	return render(request, 'prediction.html')


class AirportsViewSet(viewsets.ModelViewSet):
    queryset = Airports.objects.all()
    serializer_class = AirportsSerializer



class CarriersViewSet(viewsets.ModelViewSet):
    queryset = Carriers.objects.all()
    serializer_class = CarriersSerializer

class DatasetRawViewSet(viewsets.ModelViewSet):
    queryset = DatasetRaw.objects.all()
    serializer_class = DatasetRawSerializer

class DatasetCleanViewSet(viewsets.ModelViewSet):
    queryset = DatasetClean.objects.all()
    serializer_class = DatasetCleanSerializer



class ExceptionLoggingMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(request.body)

        response = self.get_response(request)

        return response