from django.urls import path
from . import views

urlpatterns = [
    path("search/", views.search_products, name="search_products"),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
    path("simulate-update/", views.simulate_price_update),
    path("refresh/<int:product_id>/", views.refresh_product_price),
]