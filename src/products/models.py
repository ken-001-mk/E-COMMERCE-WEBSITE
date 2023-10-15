from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='products_images',blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, related_name='products', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    