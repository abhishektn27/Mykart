from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static,settings
from . import views

urlpatterns = [

    path('cart',views.show_cart,name='cart')
]
