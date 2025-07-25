from itertools import product
from lib2to3.fixes.fix_input import context

from django.shortcuts import render,get_object_or_404
from .models import Category,Product

# Create your views here.



def product_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    products=Product.objects.all()
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        products=products.filter(category=category)

    context={
        'category':category,
        'categories':categories,
        'products':products,
    }
    request.session['phone']='09131000000'
    return  render(request,'shop/list.html',context)

def product_detail(request,id,slug):
    product=get_object_or_404(Product,slug=slug,id= id)
    phone=request.session.get('phone')
    context = {
        'product':product,
        'phone':phone,
    }
    return render(request,'shop/detail.html',context)

