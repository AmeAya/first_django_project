from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Brand


class CategoryListView(ListView):
    model = Category  # Из какой модельки брать данные
    context_object_name = 'Categories'  # Как назвать переменную с этими данными
    template_name = 'category_list_template.html'  # Имя html файла куда отправить данные


class BrandListView(ListView):
    model = Brand
    context_object_name = 'Brands'
    template_name = 'brand_list_template.html'


# 1) Создать ListView для брендов в first_app/views.py
# 2) Создать template для брендов в templates/
# 3) В темплейте для брендов создать цикл, и в нем выгрузить все name в templates/..
# 4) Провести url маршрут в core/urls.py
