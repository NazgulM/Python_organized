from django.urls import path, include
from .views import fortune

urlpatterns = [
    path("", fortune),
]