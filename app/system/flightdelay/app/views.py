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
import time
from sklearn.preprocessing import LabelEncoder


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

def json_predict(request):
    # LR = LinearRegression
    # RFR = RandomForestRegressor
    # ETR = ExtraTreesRegressor
    # DTR = DecisionTreeRegressor

    start_time = time.time()
    dataset_clean = library.dataset_clean()
    encoder = LabelEncoder()
    dataset_clean['carrier'] = encoder.fit_transform(dataset_clean['carrier'])
    dataset_clean['airport'] = encoder.fit_transform(dataset_clean['airport'])
    train_test = library.split_data(dataset_clean)
    context = library.predict(request.GET.get('type'), train_test)
    execution_time = round(time.time() - start_time, 2) 

    context['execution_time'] = execution_time
    return JsonResponse(context, safe=False)

def json_split_data(request):
    dataset_clean = library.dataset_clean()
    x_train,x_test,y_train,y_test = library.split_data(dataset_clean)
    x_train,x_test,y_train,y_test = library.split_data(dataset_clean)
    data_train = x_train.merge(y_train.to_frame(), left_index=True, right_index=True)
    data_test = x_test.merge(y_test.to_frame(), left_index=True, right_index=True)
    data_train = json.loads(data_train.to_json(orient="records"))
    data_test = json.loads(data_test.to_json(orient="records"))
    context = {
         'data_train' : data_train,
         'data_test' : data_test,
    }
    return JsonResponse(context, safe=False)


def statistik(request):
    return render(request, 'statistik.html')

def json_statistik(request):
     
     dataset = library.dataset_clean()
     flights_per_month = library.get_plot_flights_per_month(dataset)
     most_number_of_flights = library.get_plot_most_number_of_flights(dataset)

     context = {
          "flights_per_month": flights_per_month,
          "most_number_of_flights": most_number_of_flights
     }
     return JsonResponse(context, safe=False)

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