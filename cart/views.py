from http.client import responses, HTTPException

from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from kavenegar import *

from shop.models import Product
from .cart import Cart
from django.http import JsonResponse

# Create your views here.

@require_POST
def add_to_cart(request, product_id):
    try:
        cart=Cart(request)
        product=get_object_or_404(Product, id=product_id)
        cart.add(product)
        context={
            'item_count': len(cart),
            'total_price': cart.get_total_price(),
        }
        #-----------------------
        try:
            api=KavenegarAPI('4D597A707341464C394F4E7075534D65364364484A61576A2F313054705173594A2F4A474738567A7541413D')
            params={
                'sender': '2000660110',
                'receptor':'09963140715',
                'message':f' محصول {str(product)} به سبد خرید اضافه شد. ',
            }
            response=api.sms_send(params)
            print(response)
        except APIException as e:
            print(e)
        except HTTPException as e:
            print(e)

        #------------------------
        return JsonResponse(context)
    except:
        return JsonResponse({"error":"Invalid request."})

def cart_detail(request):
    cart=Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

@require_POST
def update_quantity(request):
    item_id=request.POST.get('item_id')
    action=request.POST.get('action')
    try:
        product=get_object_or_404(Product, id=item_id)
        cart=Cart(request)
        if action=='add':
            cart.add(product)
        elif action=='decrease':
            cart.decrease(product)

        context={
            'item_count': len(cart),
            'total_price': cart.get_total_price(),

            'quantity':cart.cart['item_id']['quantity'],
            # 'price':cart.cart[item_id]['price'],
            'total':cart.cart[item_id]['quantity']*cart.cart[item_id]['price'],
            'final_price':cart.get_final_price(),
            'success':True,
        }
        return JsonResponse(context)
    except:
        return JsonResponse({'success':False,'error':'Item not found!'})

@require_POST
def remove_item(request):
    item_id=request.POST.get('item_id')
    try:
        product=get_object_or_404(Product, id=item_id)
        cart=Cart(request)
        cart.remove(product)

        context={
            'item_count': len(cart),
            'total_price': cart.get_total_price(),
            'final_price':cart.get_final_price(),
            'success':True,
        }
        return JsonResponse(context)
    except:
        return JsonResponse({'success':False,'error':'Item not found!'})
