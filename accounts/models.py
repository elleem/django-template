from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse

class Profile(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='user_profile')
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

#new user model
class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=160, unique=True)
    username = models.CharField(max_length=50, unique=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.username


# basic database modeling that can be applied per application
class Database(models.Model):
    item = models.CharField(max_length=64)
    userid = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    image_url = models.URLField(default='none')

    def __str__(self):
        return self.item

#return user to the detail page of their new entry
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])