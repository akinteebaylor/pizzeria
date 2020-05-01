from django.db import models

# Create your models here.
class Pizza(models.Model):
    """A Pizza Type."""
    name = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class Topping(models.Model):
    """A topic the user is learning about."""
    name = models.CharField(max_length=200)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class pizza_comment(models.Model):
    Pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}..." 
        