from django.shortcuts import render


def index(request):
    """Домашняя страница приложения learning log."""
    return render(request, 'meal_plans/index.html')
# Create your views here.
