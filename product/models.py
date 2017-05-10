from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=[str(self.slug)])


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateField()
    modified_at = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', args=[str(self.category.slug), str(self.slug)])