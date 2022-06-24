from django.db import models
from datetime import date


class RestaurantList(models.Model):
    name = models.CharField(max_length=80)
    location = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class FoodMenu(models.Model):
    restaurant = models.ForeignKey(RestaurantList, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=80)

    def __str__(self):
        return self.food_name


class User(models.Model):
    user_name = models.CharField(max_length=100)
    order_date = models.DateField(default=date.today())
    lunch = models.ForeignKey(FoodMenu, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name
