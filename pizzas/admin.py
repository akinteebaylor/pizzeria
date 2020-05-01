from django.contrib import admin

# Register your models here.
from .models import Pizza, Topping, pizza_comment
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(pizza_comment)
