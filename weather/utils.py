import requests
# import pandas as pd
from datetime import datetime
from weather.models import WeatherSummary
from django.conf import settings

def fetch_weather_data(city):
    api_key = settings.ycebfd4f85018aa5b38c26a703d1692b5

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'  # Using metric for Celsius

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses (4xx, 5xx)
        return response.json()  # Return the JSON response if successful
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Log the HTTP error
    except Exception as err:
        print(f'An error occurred: {err}')  # Log any other errors
    return None  # Return None if there was an error


def save_daily_summary(date, temp_list, conditions):
    avg_temp = sum(temp_list) / len(temp_list)
    max_temp = max(temp_list)
    min_temp = min(temp_list)
    dominant_condition = max(set(conditions), key=conditions.count)

    summary = WeatherSummary(
        date=date,
        avg_temp=avg_temp,
        max_temp=max_temp,
        min_temp=min_temp,
        dominant_condition=dominant_condition,
    )
    summary.save()