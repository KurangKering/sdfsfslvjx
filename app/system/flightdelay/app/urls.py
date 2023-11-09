from django.urls import path
from . import views

urlpatterns = [
    path('data-master/airports', views.airports, name="airports"),
    path('data-master/carriers', views.carriers, name="carriers"),
    path('dataset-raw', views.dataset_raw, name="dataset-raw"),
    path('dataset-clean', views.dataset_clean, name="dataset-clean"),
    path('classifier', views.classifier, name="classifier"),
    path('prediction', views.prediction, name="prediction"),
    path('json_dataset_clean', views.json_dataset_clean, name="json_dataset_clean"),
    path('json_predict', views.json_predict, name="json_predict"),
]
