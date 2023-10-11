from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('icecream/<int:pk>/', views.icecream_detail, name='icecream_detail'),
]
