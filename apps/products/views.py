#from django.shortcuts import render
# Create your views here.


from rest_framework.generics import ListAPIView
from rest_framework import viewsets, permissions

from .models import ProductModel
from .serializers import ProductSerializer

class ProductListAPIView(ListAPIView):

    queryset = ProductModel.objects.filter(stock=True)

    serializer_class = ProductSerializer



class ProductViewSet(viewsets.ModelViewSet):
    
    queryset = ProductModel.objects.all()

    permission_classes = [permissions.IsAdminUser]

    serializer_class = ProductSerializer