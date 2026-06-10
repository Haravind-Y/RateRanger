from .amazon import get_price as amazon_price
from .flipkart import get_price as flipkart_price


def get_latest_price(product):
    if "amazon" in product.product_url.lower():
        return amazon_price(product.product_url)

    if "flipkart" in product.product_url.lower():
        return flipkart_price(product.product_url)

    return None