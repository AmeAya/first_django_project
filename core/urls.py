"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from first_app.views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration', UserCreateView.as_view(), name='registration_url'),
    path('category_list', CategoryListView.as_view(), name='category_list_url'),
    path('brand_list', BrandListView.as_view(), name='brand_list_url'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail_url'),
    path('brand_detail/<int:pk>', BrandDetailView.as_view(), name='brand_detail_url'),
    path('create_brand', BrandCreateView.as_view(), name='create_brand_url'),
    path('create_product', ProductCreateView.as_view(), name='create_product_url'),
    path('brand_update/<int:pk>', BrandUpdateView.as_view(), name='update_brand_url'),
    path('brand_delete/<int:pk>', BrandDeleteView.as_view(), name='delete_brand_url'),
    path('product_list', ProductListView.as_view(), name='product_list_url'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update_url'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete_url'),
    path('', HomeTemplateView.as_view(), name='home_url'),
    # <int:pk> - Означает что здесь в юрле должна быть переменная pk типа integer
]

# path('<route>', <view>)
# <route> - Маршрут в ссылке
# <view> - Вью которая обрабатывает этот маршрут
# Если <view> написан через Class то тогда .as_view()


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
