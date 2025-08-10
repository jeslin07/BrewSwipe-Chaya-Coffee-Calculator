from django.urls import path
from . import views

urlpatterns = [
    path("", views.chaya_coffee_calculator, name="chaya_coffee"),
]
