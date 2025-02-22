from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import FavoriteCity
import requests
from django.core.cache import cache

# Index request
def index(request):
    api_key = "bd5e378503939ddaee76f12ad7a97608"  # Replace with your API key
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    city = request.GET.get('city')

    weather_data = {}
    forecast_data = {}

    try:
        if city:
            request.session['city'] = city
            # Fetch weather data by city name
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            weather_response = requests.get(weather_url, timeout=5)  # Add timeout
            if weather_response.status_code == 200:
                weather_data = weather_response.json()

            # Fetch 7-day forecast data
            forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
            forecast_response = requests.get(forecast_url, timeout=5)  # Add timeout
            if forecast_response.status_code == 200:
                forecast_data = forecast_response.json()

        elif lat and lon:
            # Fetch weather data by coordinates
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
            weather_response = requests.get(weather_url, timeout=5)  # Add timeout
            if weather_response.status_code == 200:
                weather_data = weather_response.json()

            # Fetch 7-day forecast data
            forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
            forecast_response = requests.get(forecast_url, timeout=5)  # Add timeout
            if forecast_response.status_code == 200:
                forecast_data = forecast_response.json()

    except requests.exceptions.RequestException as e:
        # Handle connection errors
        print(f"Error fetching weather data: {e}")
        weather_data = {}
        forecast_data = {}

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

# User Authentication Views
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'weather/login.html', {'error': 'Invalid credentials'})
    return render(request, 'weather/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def add_favorite_city(request):
    if request.method == 'POST':
        city = request.POST['city']
        country = request.POST['country']
        FavoriteCity.objects.create(user=request.user, city=city, country=country)
        return redirect('index')
    return render(request, 'weather/add_favorite_city.html')

@login_required
def favorite_cities(request):
    favorite_cities = FavoriteCity.objects.filter(user=request.user)
    return render(request, 'weather/favorite_cities.html', {'favorite_cities': favorite_cities})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('index')  # Redirect to the home page
    else:
        form = UserCreationForm()
    return render(request, 'weather/register.html', {'form': form})