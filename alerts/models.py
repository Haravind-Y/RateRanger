from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    target_price = models.DecimalField(max_digits=10, decimal_places=2)

    is_triggered = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - {self.target_price}"