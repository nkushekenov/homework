from django.db import models

class IceCream(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    flavor = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Kiosk(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    ice_creams = models.ManyToManyField(IceCream, related_name='kiosks')

    def __str__(self):
        return self.name

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

