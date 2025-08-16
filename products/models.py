from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=100)   # e.g., "Berlin Showroom"
    city = models.CharField(max_length=100)   # e.g., "Berlin"
    address = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.city})"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    locations = models.ManyToManyField(Location, related_name="products", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

