from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
from datetime import datetime, timedelta
from weather.utils import fetch_weather_data
from .models import DailyWeather

def weather_summary_view(request):
    cities = request.GET.get('cities', '')  # Get the 'cities' parameter from the request
    api_key = 'cebfd4f85018aa5b38c26a703d1692b5'  # Replace with your actual API key
    weather_data_list = []  # List to store weather data for each city
    summaries = []  # This will hold daily weather summaries
    weather_data = DailyWeather.objects.all()

    print(weather_data)

    if cities:  # If cities are provided in the query
        # Split the cities by commas and strip any extra spaces
        city_list = [city.strip() for city in cities.split(',')]

        for city in city_list:  # Iterate over each city
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise an error for bad responses
                weather_data = response.json()  # Parse the JSON response
                weather_data_list.append(weather_data)  # Add the data to the list

                # Simulated daily summary data for the example (replace with actual fetching logic)
                summary = {
                    'date': (datetime.now() - timedelta(days=len(summaries))).date(),  # Simulated date
                    'avg_temp': weather_data['main']['temp'],  # Placeholder for average temperature
                    'max_temp': weather_data['main']['temp_max'],  # Placeholder for max temperature
                    'min_temp': weather_data['main']['temp_min'],  # Placeholder for min temperature
                    'dominant_condition': weather_data['weather'][0]['description'],
            }
                summaries.append(summary)
            except requests.exceptions.HTTPError as err:
                print(f"HTTP error occurred for {city}: {err}")  # Print HTTP error
            except Exception as e:
                print(f"Error occurred for {city}: {e}")  # Print any other error

    # Render the template with the weather data list
    context = {
        'weather_data_list': weather_data_list,  # Pass the list of weather data
        'cities': cities,  # Pass the user input back to the template for display
        'summaries': summaries,
        'weather_data': weather_data,  # Pass the data to the template
        
    }

    return render(request, 'weather/summary.html', context)


def home_view(request):
    return render(request, 'weather/home.html')  # Create a home.html template


def test_api_connection(request):
    city = "Delhi,Mumbai"  # Specify the city for testing
    weather_data_list = []  # List to store weather data

    for city in city.split(','):  # Split cities for testing
        weather_data = fetch_weather_data(city.strip())  # Assuming fetch_weather_data handles the API call
        weather_data_list.append(weather_data)

    return render(request, 'weather/test_api.html', {'weather_data_list': weather_data_list})  # Pass the list of data
