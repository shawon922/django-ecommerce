from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save

from products.utils import unique_slug_generator


class Tag(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
@receiver(pre_save, sender=Tag)
def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
