
from django.db import models
class Company(models.Model):
    rank = models.IntegerField()
    name = models.CharField(max_length=255)
    revenue = models.CharField(max_length=255)
    employees = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)

    def __str__(self):
        return self.name
