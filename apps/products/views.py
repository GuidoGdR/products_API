#from django.shortcuts import render
# Create your views here.


from rest_framework.generics import ListAPIView
from rest_framework import viewsets, permissions

from rest_framework.response import Response

from .models import ProductModel
from .serializers import ProductSerializer

#Tools
def show_caregory_first(data:list[dict["category"]]) -> dict:

    finally_dic = {}
    for dic in data:
        
        if dic["category"] in finally_dic.keys():
            finally_dic[dic["category"]] += [dic]

        else:
            finally_dic[dic["category"]] = [dic]

    return finally_dic

#views
class ProductViewSet(viewsets.ModelViewSet):

    queryset = ProductModel.objects.filter(stock=True)

    serializer_class = ProductSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        
        finally_dic = show_caregory_first(serializer.data)

        return Response(finally_dic)

class ProductAdminViewSet(viewsets.ModelViewSet):
    
    queryset = ProductModel.objects.all()

    permission_classes = [permissions.IsAdminUser]

    serializer_class = ProductSerializer