"""Определяет схемы URL для learning_logs."""
from django.urls import path
from . import views

app_name = 'meal_plans'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
]