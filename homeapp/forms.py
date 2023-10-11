from django import forms
from .models import IceCream

class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ['name', 'price', 'flavor']

