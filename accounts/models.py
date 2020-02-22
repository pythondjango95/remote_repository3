from django.db import models
class Customers(models.Model):
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    mobile=models.BigIntegerField(null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    created_date=models.DateField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.first_name

class Products(models.Model):
    CATRGORY_CHOICE = (
        ('indoor','Indoor'),
        ('outdoor','Outdoor'),
        ('anywhere','Anywhere')
    )
    name = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    created_date = models.DateField(auto_now_add=True,null=True,blank=True)
    category = models.CharField(choices=CATRGORY_CHOICE,max_length=100,
                                null=True,blank=True)
    def __str__(self):
        return self.name

class Orders(models.Model):
    STATUS_CHOICES = (
        ('delivered','Delivered'),
        ('pending','Pending'),
        ('outfordelivery','Outfordelivery')
    )
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES,max_length=100)
    created_date = models.DateField(auto_now_add=True)

