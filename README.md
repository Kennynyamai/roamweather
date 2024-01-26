# ROAMWEATHER

Web application for current and forecast weather information for any city in the world

## Overview
The Weather Forecast Web Application is a user-friendly web app designed to provide real-time weather conditions and a five-day weather forecast for any city in the world. Users can effortlessly access weather information by simply entering the city name in the search bar. The application fetches data from the OpenWeatherMap API, offering comprehensive details such as the general weather description, temperature, humidity, and pressure. The forecast specifically focuses on noon weather for the next five days, ensuring users get the most relevant and timely information. With a clean and intuitive interface, this web application aims to make checking the weather a hassle-free experience for users worldwide.


## Usage


[PROJECT LINK](https://weatherroam.pythonanywhere.com/)

## Getting Started

1. Clone the repository

```bash
git clone https://github.com/Kennynyamai/roamweather.git
```
2. Create a virtual environment

```bash
python -m venv venv
```
3. Activate virtual environment


windows

```bash
venv\Scripts\activate

```
On macOS/Linux:
```bash
source venv/bin/activate

```

4. Install dependencies

```bash
pip install -r requirements.txt

```
5.  Obtain an API key from OpenWeatherMap and insert it in the settings.py file:
```bash
OPENWEATHERMAP_API_KEY = 'your_api_key'

```
6. Apply Migrations
```bash
python manage.py migrate


```
7. Run the development server
```bash
python manage.py runserver

```
8. Open your web browser and navigate to http://localhost:8000 to access the Weather Forecast Web Application.


## API KEYS
```python
# Current Weather
https://api.openweathermap.org/data/2.5/weather?id={city id}&appid={API key}

# Forecast Weather
https://api.openweathermap.org/data/2.5/forecast?id={city id}&appid={API key}


```
## Technologies used
1. Django Framework
for Backend
2. Pythonanywhere for hosting

The weather forecast data is only available for noon (midday) hours
## Limitations

The weather forecast data is only available for noon (midday) hours

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
## Acknowledgments
[OPENWEATHERMAP.ORG](https://openweathermap.org/)
## Contact

[Personal Website](https://kennedymwendwa.framer.website/)


## License

[MIT](https://choosealicense.com/licenses/mit/)

