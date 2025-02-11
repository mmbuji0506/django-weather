from django.shortcuts import render
import requests
from django.core.cache import cache

#Index request
def index(request):
    api_key = "bd5e378503939ddaee76f12ad7a97608"
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    city = request.GET.get('city')

    weather_data = {}
    forecast_data = {}
    
    #Save city search
    if city:
        request.session['city'] = city
        # Fetch weather data by city name
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        weather_response = requests.get(weather_url)
        city_to_use = request.session.get('city', 'Default City')
        weather_data = fetch_weather_data(city_to_use, api_key)

        
        if weather_response.status_code == 200:
            weather_data = weather_response.json()

        # Fetch 7-day forecast data
        forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
        forecast_response = requests.get(forecast_url)
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()

    #Fetch weather based on coordinates
    elif lat and lon:
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        weather_response = requests.get(weather_url)
        if weather_response.status_code == 200:
            weather_data = weather_response.json()

        forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        forecast_response = requests.get(forecast_url)
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()

    return render(request, 'weather/index.html', {'weather': weather_data, 'forecast': forecast_data})
def fetch_weather_data(city, api_key, session=None, cache_timeout=600): 
    """Fetch weather data from OpenWeather API with Django caching."""
    cache_key = f"weather_{city.lower()}"  # Unique cache key for each city
    cached_data = cache.get(cache_key)  # Check if data exists in cache

    if cached_data:
        return cached_data  # Return cached data if available

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        if session:
            response = session.get(weather_url, timeout=5)  # Use existing session
        else:
            response = requests.get(weather_url, timeout=5)  # Set timeout

        response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)

        data = response.json()
        if "main" in data:  # Validate response structure
            cache.set(cache_key, data, timeout=cache_timeout)  # Store in cache
            return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")  # Log the error

    return {}  # Return empty dict on failure
