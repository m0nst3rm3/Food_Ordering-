from django.urls import path
from Rms_app.views import home, user_order, final_order, index

urlpatterns = [
    path('', index, name='index'),
    path('home_page', home, name='home'),
    path('<int:restaurant_id>/', user_order, name='user_order'),
    path('<int:restaurant_id>/final_order/', final_order,
         name='final_order'),

]
