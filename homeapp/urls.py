from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('icecream/', views.icecream_list, name='icecream_list'),
    path('icecream/<int:pk>/', views.icecream_detail, name='icecream_detail'),
    path('add/', views.add_icecream, name='add_icecream'),
    
]
