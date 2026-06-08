from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def login_view(request):
    username = request.GET.get("username")
    password = request.GET.get("password")

    user = authenticate(
        request,
        username=username,
        password=password
    )

    if user:
        login(request, user)

        return JsonResponse({
            "message": "Login successful"
        })

    return JsonResponse({
        "message": "Invalid credentials"
    })


def logout_view(request):
    logout(request)

    return JsonResponse({
        "message": "Logged out"
    })