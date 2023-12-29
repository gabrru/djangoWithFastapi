from django.db import models
from django.utils import timezone

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    

class Item(models.Model):
    title = models.CharField(max_length=50)
    amount = models.IntegerField()
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
