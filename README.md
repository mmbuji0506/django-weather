# Weather Dashboard

A live weather dashboard built with Django that displays real-time weather data, weekly forecasts, and interactive maps. It provides users with an intuitive interface to track weather conditions in various locations.

## Features
- **Current Weather**: Displays temperature, humidity, wind speed, and weather conditions.
- **Weekly Forecast**: Shows weather predictions for the next 7 days with detailed metrics.
- **Hourly Forecast**: Provides weather updates for the next 12 hours.
- **Interactive Map**: Displays the location of the searched city using map integration.
- **User Authentication**: Users can log in, save favorite cities, and view weather details quickly.
- **Search Functionality**: Users can search for weather information of any city worldwide.
- **Real-Time Updates**: Weather data is updated dynamically for accuracy.
- **Dark Mode Support**: Allows users to switch between light and dark mode.
- **Mobile-Friendly Design**: Fully responsive for seamless usage on various devices.

## Technologies Used
- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **API**: OpenWeatherMap API (for fetching weather data)
- **Database**: PostgreSQL (or SQLite for development)
- **Mapping**: Leaflet.js or Google Maps API

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- Virtualenv (optional but recommended)

### Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/mmbuji0506/weather-dashboard.git
   cd weather-dashboard
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv weather-env
   source venv/bin/activate  # On Windows use `weather-env\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables (create a `.env` file and add your API keys):
   ```
   OPENWEATHER_API_KEY="bd5e378503939ddaee76f12ad7a97608"
   SECRET_KEY='django-insecure-ps%#-oo5(c-5l(!hk)^&n%0zl(gcvc2j51j4lgi4r=gs73_*!x'
   DEBUG=True
   ```
5. Apply migrations:
   ```bash
   python manage.py makemigrations
   ```
   python manage.py migrate
   ```
7. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```
8. Run the server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Open `http://127.0.0.1:8000/` in your browser.
- Search for a city to view its weather details.
- Register/login to save favorite cities.
- Explore the interactive map to visualize locations.

## Contribution
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Commit changes: `git commit -m "Add new feature"`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries or support, call +255 716 399 739/747 330 049 or reach out to mmbujijosameneza@gmail.com or visit the GitHub repository [here](https://github.com/mmbuji0506/weather-dashboard).
