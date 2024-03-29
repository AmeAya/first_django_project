from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Category, Brand, Product
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm


# Написать слледующие вьюшки:
# 1) AllBrandsView - Вью, которая рендерит все из модельки Brand
# 2) BigProductView - Вью, которая рендерит все из модельки Product с price > 1000
# 3) RandomColor - Вью, которая рендерит любую запись из модельки Color
# Для всех вью, можно как создать новый темплейт, так и использовать старый, который подходит

def dataFilterView(request, max_price):
    products = Product.objects.filter(price__lte=max_price)
    context = {
        'Products': products
    }
    return render(request=request, template_name='product_list_template.html', context=context)


def getTestView(request):
    product = Product.objects.get(id=2)
    # get - Возвращает только 1 объект
    # Если по условию найдено 0 то ошибка
    # Если по условию найдено больше чем 1 то ошибка
    context = {
        'Product': product
    }
    return render(request=request, template_name='test_template.html', context=context)


def filterView(request):
    products = Product.objects.filter(price__lte=1000)
    # objects.filter - Возвращает QuerySet из указанной модельки, состоящий из объектов подходязих по указанному фильтру
    # price__lte => price - Название поля, lte - less than or equal - Меньше или равно
    # gte - greater than or equal - Больше или равно
    # lt - less than - Меньше чем
    # gt - greater than - Больше чем
    # ne - not equal - Не равно
    context = {
        'Products': products
    }
    return render(request=request, template_name='product_list_template.html', context=context)


def customView(request):
    categories = Category.objects.all()
    # Category.objects.all() - Запрос в таблицу Category "Вернуть все записи" (Select *)
    brands = Brand.objects.all()
    context = {
        'Cats': categories,
        'Brs': brands,
        'Message': 'Hello!'
    }
    return render(request=request, template_name='custom_template.html', context=context)


class UserCreateView(CreateView):  # Registration View
    form_class = UserCreationForm  # model не надо указывать, так как она указана в формочке UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/user_create_template.html'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete_template.html'
    context_object_name = 'Product'
    success_url = reverse_lazy('product_list_url')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update_template.html'
    fields = '__all__'
    context_object_name = 'Product'
    success_url = reverse_lazy('product_list_url')


class ProductListView(ListView):
    model = Product
    template_name = 'product_list_template.html'
    context_object_name = 'Products'


class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'brand_delete_template.html'
    success_url = reverse_lazy('brand_list_url')
    context_object_name = 'Brand'


class BrandUpdateView(UpdateView):
    model = Brand
    template_name = 'brand_update_template.html'
    fields = '__all__'
    success_url = reverse_lazy('brand_list_url')
    context_object_name = 'Brand'


class HomeTemplateView(TemplateView):
    template_name = 'home.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create_template.html'
    fields = '__all__'
    success_url = reverse_lazy('product_list_url')


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'brand_detail_template.html'
    context_object_name = 'Brand'


class BrandCreateView(CreateView):
    model = Brand
    template_name = 'brand_create_template.html'
    fields = ['name']
    # fields = '__all__'  # Чтобы выгрузить все поля в form
    success_url = reverse_lazy('brand_list_url')
    # reverse_lazy - Переадресация только после завершения создания бренда


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'Product'  # Если забыть написать, то стандартное имя object
    template_name = 'product_detail_template.html'


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
