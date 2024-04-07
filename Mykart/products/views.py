from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featured_products = Product.objects.order_by('priority')[:3]
    latest_products = Product.objects.order_by('-id')[:3]
    context={
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    print(context)
    return render(request,'index.html',context)

def list_products(request):
    """



    :param request:
    :return:
    """
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Product.objects.order_by('-priority')
    product_paginator=Paginator(product_list,2)
    product_list=product_paginator.get_page(page)
    context={'Products':product_list}
    return render(request,'products.html',context)

def detail_product(request,id):
    product=Product.objects.get(id=id)
    context={'product':product}
    return render(request,'product_detail.html',context)