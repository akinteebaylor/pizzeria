from django.urls import path
from . import views
app_name = 'pizzas'
urlpatterns = [
    path('', views.index, name='index'),
    path('Pizzas/', views.Pizzas, name= 'Pizzas'),
    path('topping/<int:Pizza_id>/', views.topping, name= 'topping'),   
    path('pizzacomments/<int:Pizza_id>/', views.pizzacomments, name= 'pizzacomments')   
   ]
