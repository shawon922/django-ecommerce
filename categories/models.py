from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    parent = models.ForeignKey(
        'self', on_delete=models.PROTECT, blank=True, null=True, related_name='categories')
    updated_at = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
    
    
    def __str__(self):
        return self.name
