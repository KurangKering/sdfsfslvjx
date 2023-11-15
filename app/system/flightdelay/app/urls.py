from django.urls import path
from . import views

urlpatterns = [
    path('data-master/airports', views.airports, name="airports"),
    path('data-master/carriers', views.carriers, name="carriers"),
    path('dataset-raw', views.dataset_raw, name="dataset-raw"),
    path('dataset-clean', views.dataset_clean, name="dataset-clean"),
    path('json_statistik', views.json_statistik, name="json_statistik"),
    path('statistik', views.statistik, name="statistik"),
    path('classifier', views.classifier, name="classifier"),
    path('prediction', views.prediction, name="prediction"),
    path('json_dataset_clean', views.json_dataset_clean, name="json_dataset_clean"),
    path('json_predict', views.json_predict, name="json_predict"),
    path('json_split_data', views.json_split_data, name="json_split_data"),
]
