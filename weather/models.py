from django.db import models
from django.contrib.auth.models import User

class FavoriteCity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user
    city = models.CharField(max_length=100)  # City name
    country = models.CharField(max_length=100)  # Country name

    def __str__(self):
        return f"{self.city}, {self.country}"