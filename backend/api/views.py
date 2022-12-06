import json
from products.models import Product
from products.serializers import ProductSeriallizer
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()
    
    data = {}
    if instance:
        data = ProductSeriallizer(instance).data
    return Response(data)