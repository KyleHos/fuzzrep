from django.db import models

class Submit(models.Model):
    pet_name = models.CharField(max_length=40)
    species = models.CharField(max_length=30)
    age = models.IntegerField(100)
    color = models.CharField(max_length=20)
    food_preference = models.CharField(max_length=100)
