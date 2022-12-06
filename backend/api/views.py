import json
import logging
from products.models import Product
from products.serializers import ProductSeriallizer
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    seriallerizr = ProductSeriallizer(data=request.data)
    if seriallerizr.is_valid(raise_exception=True):
        # instance = seriallerizr.save()
        data = seriallerizr.data
        return Response(data)
    return Response({'invaild': 'not invaild'}, status=400)