"""flightdelay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from rest_framework import routers
from app import views as appViews
from . import views


router = routers.DefaultRouter()
router.register(r'airports', appViews.AirportsViewSet)
router.register(r'carriers', appViews.CarriersViewSet)
router.register(r'dataset-raw', appViews.DatasetRawViewSet)
router.register(r'dataset-clean', appViews.DatasetCleanViewSet)

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    re_path(r'^api/', include(router.urls)),
    path('app/', include('app.urls')),
]
