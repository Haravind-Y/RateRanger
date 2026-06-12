from django.core.management.base import BaseCommand

from products.models import Product
from products.services import update_product_price

from scraper.service import get_latest_price


class Command(BaseCommand):

    help = "Refresh prices for all products"

    def handle(self, *args, **kwargs):

        products = Product.objects.all()

        for product in products:

            latest_price = get_latest_price(product)

            if latest_price is not None:

                update_product_price(
                    product.id,
                    latest_price
                )

                self.stdout.write(
                    self.style.SUCCESS(
                        f"{product.name} -> {latest_price}"
                    )
                )