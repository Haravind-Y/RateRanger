from .models import Product, PriceHistory
from alerts.services import check_alerts


def update_product_price(product_id, new_price):
    product = Product.objects.get(id=product_id)

    # If price actually changed
    if product.current_price != new_price:

        # update product price
        product.current_price = new_price
        product.save()

        # add history record
        PriceHistory.objects.create(
            product=product,
            price=new_price
        )
        check_alerts(product)

    return product