from django.db import models
from . models import *
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    name=models.TextField()


class Products(models.Model):
    name=models.TextField()
    image=models.FileField()
    price=models.IntegerField()
    size=models.IntegerField()
    stock=models.IntegerField()
    category=models.ForeignKey(category,on_delete=models.CASCADE)


class shop_user(models.Model):
    name=models.TextField()
    email=models.TextField()
    phno=models.IntegerField()
    username=models.TextField()
    password=models.IntegerField()


class cartitems(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    totalprice=models.IntegerField()


class buy(models.Model):
    cartitems=models.ForeignKey(cartitems,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.IntegerField()
    address=models.TextField()
    pincode=models.IntegerField()
    phno=models.IntegerField()
    state=models.TextField()
    landmark=models.TextField()
    bookingdate=models.DateField(auto_now=True)
    orderstatus=models.BooleanField(default=True)


