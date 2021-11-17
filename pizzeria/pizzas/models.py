from django.db import models


class Pizza(models.Model):
    name = models.CharField("names of types of pizza", max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField("pizza content", max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'topping'

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.name
