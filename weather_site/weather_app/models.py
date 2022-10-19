from django.db import models


class City_Weather(models.Model):
    city_state = models.CharField(max_length=200)
    temperature_low = models.TextField()
    temperature_high = models.TextField()
    weather_main = models.TextField()
    weather_description = models.TextField()
