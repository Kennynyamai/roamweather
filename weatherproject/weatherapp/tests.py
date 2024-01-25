from django.test import TestCase
from django.urls import reverse
from .forms import CitySearchForm

class WeatherAppTests(TestCase):
    def test_home_view_with_valid_city(self):
        # Test the home view with a valid city in the query parameter
        response = self.client.get(reverse('home'), {'city': 'Nairobi'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weatherapp/home.html')
        self.assertContains(response, 'Nairobi')  # Check if the city name is in the response

    def test_home_view_with_invalid_city(self):
        # Test the home view with an invalid city in the query parameter
        response = self.client.get(reverse('home'), {'city': 'InvalidCity'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weatherapp/home.html')
        self.assertContains(response, 'Error fetching weather data')  # Check for error message

    def test_weather_forecast_view_with_valid_city(self):
        # Test the weather forecast view with a valid city in the query parameter
        response = self.client.get(reverse('weather_forecast'), {'city': 'Nairobi'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weatherapp/weather_forecast.html')
        self.assertContains(response, 'Nairobi')  # Check if the city name is in the response

    def test_weather_forecast_view_with_invalid_city(self):
        # Test the weather forecast view with an invalid city in the query parameter
        response = self.client.get(reverse('weather_forecast'), {'city': 'InvalidCity'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weatherapp/weather_forecast.html')
        self.assertContains(response, 'Error fetching weather forecast data')  # Check for error message
