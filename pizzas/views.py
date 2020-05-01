from django.shortcuts import render
from .models import Pizza
# Create your views here.
def index(request):
    """The home page for pizzas."""
    return render(request, 'pizzas/index.html') 

def Pizzas(request):
    "Display all Pizzas"
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/Pizzas.html',context)

def topping(request,Pizza_id):
    "Display all Pizzas"
    Pizas = Pizza.objects.get(id=Pizza_id)
    toppings =Pizas.topping_set.order_by('name')
    context = {'Pizas': Pizas, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html',context)


# def Toppings(request):
#     "Display all Toppings"
#     topping = Topping.objects.order_by('pizza')
#     context = {'Toppings': topping}
#     return render(request, 'pizzas/Toppings.html',context)

    # <a href="{% url 'pizzas:Toppings' %}"> -Toppings</a>