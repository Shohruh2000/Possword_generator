from django.urls import path
from .views import posswor_generation

urlpatterns = [
    path("",posswor_generation)
]