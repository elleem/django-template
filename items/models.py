from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models

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