
from rest_framework.response import Response

from .tools import show_caregory_first


def category_first_list_deco(decorating):
    def deco(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:

            serializer = self.get_serializer(page, many=True)
            
            finally_dic = show_caregory_first(serializer.data)

            decorating(self, request, *args, **kwargs)
            
            return self.get_paginated_response(finally_dic)
        
        serializer = self.get_serializer(queryset, many=True)
        
        finally_dic = show_caregory_first(serializer.data)
        
        decorating(self, request, *args, **kwargs)

        return Response(finally_dic)

    return deco