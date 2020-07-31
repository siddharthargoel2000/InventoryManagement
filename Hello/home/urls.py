from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('donation', views.donation, name='donation'),
    path('services', views.services, name='services'),
    path('inventory', views.inventory, name='inventory'),
    path('alerts', views.alerts , name='alerts'),
]