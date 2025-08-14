from shop.models import Product
from serializers import ProductSerializer
from rest_framework import generics

#هدفمون اینه یک سری ابجکت های مدل پروداکت ک محصولات هست را بین دو تا وبسایت منتقل کنیم باید
# برای انتقال از جیسون استفاده کنیم ک بیاد ابجکت های پیچیده مدل را به سریالایز های ساده تبدیل کنه

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


