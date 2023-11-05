from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import filters
from django.db.models import Q
import pandas as pd
import json
from django.http import JsonResponse
from app import library

# Create your views here.

def airports(request):
	return render(request, 'airports.html')

def carriers(request):
	return render(request, 'carriers.html')

def dataset_raw(request):
	return render(request, 'dataset-raw.html')

def json_dataset_clean(request):
    # process cleaning dataset and showing the output
    context = library.cleaning_dataset()
    return JsonResponse(context, safe=False)


def dataset_clean(request):

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