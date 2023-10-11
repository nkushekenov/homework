from django.db import models
from django.core.validators import MinValueValidator


class IceCream(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    flavor = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}: {self.name}"
    
    def with_tax(self):
        return self.price * 1.1 

class Kiosk(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    ice_creams = models.ManyToManyField(IceCream, related_name='kiosks')

    def __str__(self):
        return f"{self.id}: {self.name}"
    
    def total_icecream_price(self):
        return sum([icecream.price for icecream in self.icecreams.all()])

class Parent(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    parent = models.ForeignKey(Parent, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

