from django.shortcuts import render, redirect
from .models import Pizza
from .forms import Pizza_commentForm
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

def pizzacomments(request,Pizza_id):
    pizza = Pizza.objects.get(id=Pizza_id)
    if request.method != 'POST':
        form = Pizza_commentForm()
    else:
        form = Pizza_commentForm(data=request.POST)
        if form.is_valid():
            pizza_comments = form.save(commit=False)
            pizza_comments.Pizza = pizza
            pizza_comments.save()
            return redirect('pizzas:pizza', Pizza_id=Pizza_id)
    context = {'pizza': pizza, 'form': form}
    return render(request, 'pizzas/new_comment.html', context)