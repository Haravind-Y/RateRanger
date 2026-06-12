from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from products.models import Product
import numpy as np

from sklearn.linear_model import LinearRegression


def predict_price(request, product_id):
    product = Product.objects.get(id=product_id)

    prices = list(
        product.price_history.values_list(
            "price",
            flat=True
        )
    )

    if len(prices) == 0:
        return JsonResponse({
            "message": "No price history found"
        })

    prices = [float(p) for p in prices]

    current_price = float(product.current_price)

    average_price = sum(prices) / len(prices)

    # Machine Learning Prediction
    x = np.array(range(len(prices))).reshape(-1, 1)
    y = np.array(prices)

    model = LinearRegression()
    model.fit(x, y)

    next_day = np.array([[len(prices)]])
    predicted_price = model.predict(next_day)[0]

    if current_price < average_price:
        recommendation = "Good time to buy"
    elif current_price > average_price:
        recommendation = "Wait for a price drop"
    else:
        recommendation = "Fair price"

    return JsonResponse({
        "product": product.name,
        "current_price": current_price,
        "predicted_price": round(predicted_price, 2),
        "average_price": round(average_price, 2),
        "lowest_price": min(prices),
        "highest_price": max(prices),
        "recommendation": recommendation,
    })