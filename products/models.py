import os
import uuid
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.urls import reverse

from .utils import unique_slug_generator
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
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Product)
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# another way instead of @receiver decorator
# pre_save.connect(product_pre_save_receiver, sender=Product)
