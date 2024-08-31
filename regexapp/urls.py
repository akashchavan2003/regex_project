from django.urls import path
from .views import extract_numbers

urlpatterns = [
    path('extract-numbers/', extract_numbers, name='extract_numbers'),
]