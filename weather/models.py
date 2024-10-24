from django.db import models

class WeatherSummary(models.Model):
    date = models.DateField()
    avg_temp = models.FloatField()
    max_temp = models.FloatField()
    min_temp = models.FloatField()
    dominant_condition = models.CharField(max_length=50)

    def __str__(self):
        return f"Weather on {self.date}: Avg Temp: {self.avg_temp}°C, Max Temp: {self.max_temp}°C, Min Temp: {self.min_temp}°C, Condition: {self.dominant_condition}"

class AlertThreshold(models.Model):
    temperature_threshold = models.FloatField()
    city = models.CharField(max_length=100)
    alert_enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"Alert for {self.city}: Threshold {self.temperature_threshold}°C"
    

class DailyWeather(models.Model):
    date = models.DateField(unique=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    precipitation = models.FloatField()
    wind_speed = models.FloatField()

    def __str__(self):
        return f"Weather on {self.date}: {self.temperature}°C, {self.humidity}%, {self.precipitation}mm, {self.wind_speed} m/s"