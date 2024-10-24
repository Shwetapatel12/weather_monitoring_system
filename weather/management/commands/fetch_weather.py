# weather/management/commands/fetch_weather.py
import time
from django.core.management.base import BaseCommand
from weather.utils import fetch_weather
from weather.models import WeatherSummary, AlertThreshold,DailyWeather
from django.utils import timezone

class Command(BaseCommand):
    help = 'Fetch weather data from OpenWeatherMap API'

    def handle(self, *args, **kwargs):
        api_key = 'cebfd4f85018aa5b38c26a703d1692b5'  # Replace with your API key
        cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

        while True:
            for city in cities:
                weather_data = fetch_weather(city, api_key)
                self.process_weather_data(weather_data)
            time.sleep(300)  # Wait for 5 minutes

    def process_weather_data(self, weather_data):
        if weather_data.get("main"):
            temp_kelvin = weather_data["main"]["temp"]
            temp_celsius = temp_kelvin - 273.15
            # Assume you fetch other necessary data similarly
            # Calculate aggregates, save to DB, etc.
def check_alerts(city, current_temp):
    thresholds = AlertThreshold.objects.filter(city=city, alert_enabled=True)
    for threshold in thresholds:
        if current_temp > threshold.temperature_threshold:
            trigger_alert(city, current_temp)

def trigger_alert(city, temp):
    print(f"Alert: {city}'s temperature is {temp}°C, exceeding threshold!")