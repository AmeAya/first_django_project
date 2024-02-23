from django.db import models


class Category(models.Model):
    # id = # Django сам создает в каждой таблице поле id(pk) - SERIAL PK
    name = models.CharField(max_length=100)  # VARCHAR(100)


class Brand(models.Model):
    name = models.CharField(max_length=100)


class Color(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    VIN = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    # models.CASCADE - Если источник FK удалят, то удалятся все привязанные к нему записи из этой таблицы
    # models.SET_NULL - Если источник FK удалят, то в записях привязанной к нему будет стоят NULL
