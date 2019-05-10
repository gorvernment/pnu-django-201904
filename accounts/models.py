from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    ip = models.GenericIPAddressField()