
from django.db import models

#company details
class Company(models.Model):
    rank = models.IntegerField()
    name = models.CharField(max_length=255)
    revenue = models.CharField(max_length=255)
    employees = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)

    def __str__(self):
        return self.name
#for cities
class City(models.Model):
    city = models.CharField(max_length=255, default='Unknown')
    country = models.CharField(max_length=255, default='Unknown Country')
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    
    def __str__(self):
        return self.city
