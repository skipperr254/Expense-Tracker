from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    date_added = models.DateTimeField(default=timezone.now)
    owner = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    date_added = models.DateTimeField(default=timezone.now)

    
    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.name