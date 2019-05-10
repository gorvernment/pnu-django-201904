from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse

class Shop(models.Model):
    name = models.CharField(max_length=100,
                            validators=[MinLengthValidator(5)])
    photo = models.ImageField(blank=True)
    desc = models.TextField(blank=True)
    address = models.CharField(max_length=50, blank=True)

    def get_absolute_url(self):
        return reverse('shop:shop_detail', args=[self.pk])

class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
