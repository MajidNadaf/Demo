"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.urls import path,include
from .routers import *
from demo_app.views import *
from django.conf import settings
from django.conf.urls.static import static
from razorpay_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api',include(router.urls)),


    path('registration',RegistrationView,name='registration'),
    path('',Login,name='login'),
    path('logout',logout_view,name='logout'),
    path('home',home,name='home'),
    path('product',ProductView,name='product'),
    path('product_list',ProductListView,name='product_list'),
    path('update_product/<int:id>',ProductUpdateView,name='update_product'),

    path('sale',SaleView,name='sale'),
    path("product_data",product_data,name="product_data"),
    path("product_order_list",Product_list_Post,name="product_order_list"),


    path('payment',payment_home_page,name='payment')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
