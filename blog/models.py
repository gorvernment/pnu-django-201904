from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(6)])
    content = models.TextField()
    ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])

    @property
    def masked_ip(self):
        return '.'.join(self.ip.split('.')[:2] + ['*', '*'])