from django import forms

from .models import pizza_comment

class Pizza_commentForm(forms.ModelForm):
    class Meta:
        model = pizza_comment
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}