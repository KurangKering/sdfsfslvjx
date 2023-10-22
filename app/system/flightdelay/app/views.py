from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import filters
from django.db.models import Q

# Create your views here.

def airports(request):
	return render(request, 'airports.html')

def carriers(request):
	return render(request, 'carriers.html')

def flights(request):
	return render(request, 'flights.html')

def preprocessing(request):
	return render(request, 'preprocessing.html')

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

class FlightsViewSet(viewsets.ModelViewSet):
    queryset = Flights.objects.all()
    serializer_class = FlightsSerializer


class ExceptionLoggingMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(request.body)

        response = self.get_response(request)

        return response