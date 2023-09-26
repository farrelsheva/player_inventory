from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    User: models.ForeignKey(User, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    description = models.TextField()
    