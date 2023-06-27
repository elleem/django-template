from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser


#new user model
class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=160, unique=True)
    username = models.CharField(max_length=50, unique=True)
    age = models.IntegerField(null=True)
    birthday = models.DateField(null=True)
    # password = models.CharField(max_length=100)


    def __str__(self):
        return self.username


