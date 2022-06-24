from django.shortcuts import render, get_object_or_404
from .models import RestaurantList
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'Rms_app/index.html')


def home(request):
    all_restaurant = RestaurantList.objects.all()
    context = {
        'all_restaurant': all_restaurant,
        }
    return render(request, 'Rms_app/home.html', context)


def user_order(request, restaurant_id):
    restaurant = get_object_or_404(RestaurantList, pk=restaurant_id)
    food_names = restaurant.foodmenu_set.all()
    context = {
        "restaurant": restaurant,
        "food_names": food_names,
    }
    return render(request, 'Rms_app/uorder.html', context)


@login_required
def final_order(request, restaurant_id):
    if request.method == 'POST':
        ordered_food = (request.POST.get('food'))
        context = {
            'ordered_food': ordered_food
        }
        return render(request, 'Rms_app/final_order.html', context)

