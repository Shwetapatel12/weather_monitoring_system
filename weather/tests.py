from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import WeatherSummary

class WeatherModelTest(TestCase):
    def test_weather_summary_creation(self):
        summary = WeatherSummary.objects.create(date="2024-10-01", avg_temp=25.5, max_temp=30.0, min_temp=20.0, dominant_condition="Clear")
        self.assertEqual(summary.avg_temp, 25.5)
