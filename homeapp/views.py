from django.shortcuts import redirect, render

from django.shortcuts import render, get_object_or_404

from homeapp.forms import IceCreamForm
from .models import IceCream

def home(request):
    return render(request, 'home.html')

def add_icecream(request):
    if request.method == 'POST':
        form = IceCreamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('icecream_list')  # предполагается, что у вас есть URL с именем 'icecream_list'
    else:
        form = IceCreamForm()
    return render(request, 'add_icecream.html', {'form': form})


def icecream_list(request):
    icecreams = IceCream.objects.all()
    return render(request, 'icecream_list.html', {'icecreams': icecreams})

def icecream_detail(request, pk):
    icecream = get_object_or_404(IceCream, pk=pk)
    return render(request, 'icecream_detail.html', {'icecream': icecream})
