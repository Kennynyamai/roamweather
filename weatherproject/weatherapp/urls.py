from django.urls import path
from .views import home, weather_forecast

urlpatterns = [
    path('', home, name='home'),
    path('forecast/', weather_forecast, name='weather_forecast'),
]
