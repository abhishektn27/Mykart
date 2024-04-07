from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static,settings
from . import views

urlpatterns = [

    path('account',views.show_account,name='account'),
    path('logout', views.signout, name='logout')
]
