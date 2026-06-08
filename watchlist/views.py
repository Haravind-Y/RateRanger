from django.http import JsonResponse
from django.contrib.auth.models import User

from products.models import Product
from .models import Watchlist
from django.contrib.auth.decorators import login_required


@login_required
def add_to_watchlist(request):
    product_id = request.GET.get("product_id")

    user = request.user

    product = Product.objects.get(id=product_id)

    watchlist_item, created = Watchlist.objects.get_or_create(
        user=user,
        product=product
    )

    if created:
        return JsonResponse({
            "message": "Added to watchlist"
        })

    return JsonResponse({
        "message": "Already in watchlist"
    })


@login_required
def view_watchlist(request):
    user = request.user
    items = Watchlist.objects.filter(user=user)

    data = []

    for item in items:
        data.append({
            "product_id": item.product.id,
            "name": item.product.name,
            "current_price": str(item.product.current_price),
            "source": item.product.source,
        })

    return JsonResponse(data, safe=False)


@login_required
def remove_from_watchlist(request):
    product_id = request.GET.get("product_id")

    user = request.user
    product = Product.objects.get(id=product_id)

    deleted, _ = Watchlist.objects.filter(
        user=user,
        product=product
    ).delete()

    if deleted:
        return JsonResponse({"message": "Removed from watchlist"})

    return JsonResponse({"message": "Item not found in watchlist"})