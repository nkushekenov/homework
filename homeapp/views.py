from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import IceCream

def home(request):
    return render(request, 'homeapp/home.html')

def icecream_detail(request, pk):
    icecream = get_object_or_404(IceCream, pk=pk)
    return render(request, 'homeapp/icecream_detail.html', {'icecream': icecream})
