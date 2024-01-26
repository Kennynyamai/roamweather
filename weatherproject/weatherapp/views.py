from django.shortcuts import render
import requests
from datetime import datetime
from django.conf import settings
from .forms import CitySearchForm

api_key = "2714ebb41345a682c696766ecde571b4"

# Helper function to format date and time
def format_datetime(dt_txt):
    # Parse and formatting the date and time string
    dt = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
    return dt.strftime('%A, %d')

# Helper function to make API requests and handle exceptions
def make_api_request(url):
    try:
        # Making the API request and handle common exceptions
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        # Raising a more generic exception for any request-related errors
        raise Exception(f"Error fetching data: {str(e)}")

# View function for the home page
def home(request):
    
    form = CitySearchForm(request.GET)

    # Set the default city if the form is not valid
    if form.is_valid():
        city = form.cleaned_data['city']
    else:
        city = 'Nairobi'

    # Build the URL for the current weather API request
    current_weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        # Make the API request for current weather data
        current_weather_data = make_api_request(current_weather_url)

        # Extract relevant information from the API response
        weather = current_weather_data['weather']
        main = current_weather_data['main']
        city_info = current_weather_data.get('sys', {})

        
        context = {
            'weather': weather,
            'main': main,   
            'city': city,
            'city_info': city_info,
            'form': form,
        }
    except Exception as e:
        # Handle exceptions and provide an error message in the context
        context = {'error_message': str(e), 'form': form}

    # Render the home page with the context
    return render(request, 'weatherapp/home.html', context)

# View function for the weather forecast page
def weather_forecast(request):
    # Initialize the search form with GET data
    form = CitySearchForm(request.GET)

    # Set the default city if the form is not valid
    if form.is_valid():
        city = form.cleaned_data['city']
    else:
        city = 'Nairobi'


    # Build the URL for the weather forecast API request
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'

    try:
        # Make the API request for weather forecast data
        data = make_api_request(url)

        # Extract relevant information from the API response
        city_info = data.get('city', {})
        forecast_list = data.get('list', [])

        # Filter forecast entries for noon for the next five days
        noon_forecasts = []
        for entry in forecast_list:
            dt_txt = entry.get('dt_txt')
            dt = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
            if dt.hour == 12:
                entry['dt_txt'] = format_datetime(dt_txt)
                noon_forecasts.append(entry)
            if len(noon_forecasts) >= 5:
                break

        # Prepare the context for rendering the weather forecast page
        context = {
            'city_info': city_info,
            'forecast_list': noon_forecasts,
            'city': city,
            'form': form,
        }
    except Exception as e:
        # Handle exceptions and provide an error message in the context
        context = {'error_message': str(e), 'form': form}

    # Render the weather forecast page with the context
    return render(request, 'weatherapp/weather_forecast.html', context)
