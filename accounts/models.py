from django.db import models
from django.contrib.auth.models import AbstractUser


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
