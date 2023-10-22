from django.urls import path
from . import views

urlpatterns = [
    path('data-master/airports', views.airports, name="airports"),
    path('data-master/carriers', views.carriers, name="carriers"),
    path('data-master/flights', views.flights, name="flights"),
    path('classifier', views.classifier, name="classifier"),
    path('prediction', views.prediction, name="prediction"),
]
