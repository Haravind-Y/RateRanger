from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=500)
    source = models.CharField(max_length=50)
    product_url = models.URLField(unique=True)

    current_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image_url = models.URLField(blank=True)
    rating = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PriceHistory(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="price_history"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.price}"