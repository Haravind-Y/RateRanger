from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_to_watchlist, name="add_to_watchlist"),
    path("", views.view_watchlist, name="view_watchlist"),
    path("remove/", views.remove_from_watchlist, name="remove_from_watchlist"),
]