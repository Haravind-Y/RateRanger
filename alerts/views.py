from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.contrib.auth.models import User
from products.models import Product
from .models import Alert
from django.contrib.auth.decorators import login_required

@login_required
def create_alert(request):
    product_id = request.GET.get("product_id")
    target_price = request.GET.get("target_price")

    user = request.user
    product = Product.objects.get(id=product_id)

    alert, created = Alert.objects.get_or_create(
        user=user,
        product=product,
        target_price=target_price
    )

    if created:
        return JsonResponse({"message": "Alert created"})

    return JsonResponse({"message": "Alert already exists"})