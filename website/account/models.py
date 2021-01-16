from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer (models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    email= models.CharField(max_length=100,null=True)
    phone= models.CharField(max_length=100,null=True)
    photo=models.ImageField(null=True,blank=True)


    def __str__ (self):
        return self. name


class Tag(models.Model):
    name = models.CharField(max_length=100,null=True)
    def __str__ (self):
        return self. name

class Product(models.Model):
    CATOGORY={
    ('indoor','indoor'),
    ('OUT DOOR','OUT DOOR')
    }
    name=models.CharField(max_length=100,null=True)
    price=models.FloatField(null=True)
    catogory=models.CharField(max_length=100,null=True,choices=CATOGORY)
    description=models.CharField(max_length=100,null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    tag = models.ManyToManyField(Tag)

    def __str__ (self):
        return self. name
class Order(models.Model):
    STATUS={('pending','pending'),
    ('out for delivery','out for delivery'),
    ('Delivered','Delivered')
    }
    customer =models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product =models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    status= models.CharField(max_length=100,null=True,choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.product.name
