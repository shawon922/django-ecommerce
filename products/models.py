import os
import uuid
from django.db import models

from categories.models import Category


def upload_location(instance, filename):
    unique_id = uuid.uuid4()
    
    return 'products/{unique_id}_{filename}'.format(unique_id=unique_id, filename=filename)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    image = models.FileField(upload_to=upload_location, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
