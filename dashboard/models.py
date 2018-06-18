from django.db import models

# Create your models here.

class weergave(models.Model):
    id = models.IntegerField(primary_key=True)
    longitude = models.FloatField(null=True, blank=True, default=None)
    latitude = models.FloatField(null=True, blank=True, default=None)
    timestamp = models.DateField()
    temperature = models.FloatField(null=True, blank=True, default=None)
    humidity = models.FloatField(null=True, blank=True, default=None)