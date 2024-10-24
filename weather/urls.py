# weather/urls.py
from django.urls import path
from .views import weather_summary_view, test_api_connection,home_view

urlpatterns = [
    path('summary/', weather_summary_view, name='weather_summary'),
    path('test-api/', test_api_connection, name='test_api'),  # New test URL
    path('', home_view, name='home'),
    path('weather-summary/', weather_summary_view, name='weather_summary'),
]
