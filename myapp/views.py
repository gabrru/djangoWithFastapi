from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return JsonResponse({"message": "Hello from Django!"})


def create_user(request):
    print("request.post-----------------", request)
    return JsonResponse({"request":request})

