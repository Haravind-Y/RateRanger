from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product
from decimal import Decimal
from .services import update_product_price
from scraper.service import get_latest_price

def refresh_product_price(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    latest_price = get_latest_price(product)

    if latest_price is None:
        return JsonResponse({
            "error": "Unsupported source"
        }, status=400)

    update_product_price(product.id, latest_price)

    product.refresh_from_db()

    return JsonResponse({
        "message": "Price refreshed",
        "product": product.name,
        "current_price": str(product.current_price)
    })



def search_products(request):
    query = request.GET.get("q", "")

    products = Product.objects.filter(
        name__icontains=query
    )

    data = []

    for product in products:
        data.append({
            "id": product.id,
            "name": product.name,
            "price": str(product.current_price),
            "source": product.source,
        })

    return JsonResponse(data, safe=False)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    history = []

    for entry in product.price_history.all().order_by("recorded_at"):
        history.append({
            "price": str(entry.price),
            "recorded_at": entry.recorded_at.strftime("%Y-%m-%d %H:%M:%S")
        })

    data = {
        "id": product.id,
        "name": product.name,
        "source": product.source,
        "current_price": str(product.current_price),
        "rating": product.rating,
        "image_url": product.image_url,
        "price_history": history,
    }

    return JsonResponse(data)


def simulate_price_update(request):
    product_id = request.GET.get("product_id")
    new_price = request.GET.get("price")

    product = update_product_price(
        product_id=int(product_id),
        new_price=Decimal(new_price)
    )

    return JsonResponse({
        "message": "Price updated",
        "product": product.name,
        "new_price": str(product.current_price)
    })