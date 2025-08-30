from tkinter.constants import FIRST, FALSE

from shop.models import Product
from .serializers import ProductSerializer,ShopUserSerializer,UserRegistrationSerializer
from rest_framework import generics
from rest_framework import views
from account.models import ShopUser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import BasicAuthentication
from rest_framework import viewsets
from rest_framework.decorators import action
# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class ProductDetailAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False,methods=['GET'], url_path="all_discount_products", url_name="all_discount_products",
            permission_class=[IsAuthenticated],)
    def discount_products(self,request):
        min_discount = request.query_params.get("min_discount",0)
        try:
            min_discount=int(min_discount)
        except ValueError:
            return Response({"error":'Invalid value for min_discount'},status=400)
        products=self.queryset.filter(off__gt=min_discount)
        serializer=self.get_serializer(products,many=True)
        return Response(serializer.data)

class UserListAPIView(views.APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request, *args, **kwargs):
        users =ShopUser.objects.all()
        serializer=ShopUserSerializer(users, many=True)
        return Response(serializer.data)

class UserRegistrationAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = ShopUser.objects.all()
    serializer_class = UserRegistrationSerializer