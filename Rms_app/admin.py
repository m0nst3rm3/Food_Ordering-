from django.contrib import admin
from .models import RestaurantList, User, FoodMenu

# Register your models here.
admin.site.register(RestaurantList)
admin.site.register(User)
admin.site.register(FoodMenu)
