import os
import uuid
from django.db import models

from categories.models import Category


def upload_location(instance, filename):
    unique_id = uuid.uuid4()
    
    return 'products/{unique_id}_{filename}'.format(unique_id=unique_id, filename=filename)


class ProductQuerySet(models.query.QuerySet):
    def featured_qs(self):
        return self.filter(featured=True)

    def active_qs(self):
        return self.filter(active=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def featured(self):
        return self.get_queryset().featured_qs().active_qs()


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    def __str__(self):
        return self.name
