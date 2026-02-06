from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

def home(request):
    items = [
        {"id": 1, "name": "CI/CD Workshop", "description": "Learning GitHub Actions"},
        {"id": 2, "name": "Django Templates", "description": "Server-side rendering demo"},
        {"id": 3, "name": "Python Testing", "description": "Automated regression tests"},
    ]
    return render(request, 'api/index.html', {'items': items})

@api_view(['GET'])
def health_check(request):
    return Response({"status": "ok", "message": "Backend is running!"})

@api_view(['GET'])
def get_data(request):
    data = [
        {"id": 1, "name": "CI/CD Workshop", "description": "Learning GitHub Actions"},
        {"id": 2, "name": "Django API", "description": "Simple REST endpoint"},
        {"id": 3, "name": "React Frontend", "description": "Single Page Application"},
    ]
    return Response(data)
