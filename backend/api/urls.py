from django.urls import path
from .views import health_check, get_data, home

urlpatterns = [
    path('', home, name='home'),
    path('health/', health_chec, name='health_check'),
    path('data/', get_data, name='get_data'),
]
