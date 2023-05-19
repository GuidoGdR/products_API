#from django.shortcuts import render
# Create your views here.


#Views
#from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

#Permissions
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

#Models
from .models import ProductModel
from .serializers import ProductSerializer

#decorators
from .decorators import category_first_list_deco


class ProductViewSet(ReadOnlyModelViewSet):


    queryset = ProductModel.objects.filter(stock=True)

    serializer_class = ProductSerializer

    @category_first_list_deco
    def list(self, request, *args, **kwargs):
        pass

class ProductAdminViewSet(ModelViewSet):
    
    queryset = ProductModel.objects.all()
    
    #authentication_classes = [TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = ProductSerializer

    @category_first_list_deco
    def list(self, request, *args, **kwargs):
        pass