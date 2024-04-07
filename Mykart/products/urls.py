from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static,settings
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('product_list',views.list_products,name='list_product'),
    path('product_details/<int:id>/',views.detail_product,name='detail_product')
]
