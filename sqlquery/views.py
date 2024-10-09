from django.core.serializers import serialize

from .models import Product
import json
from django.http import JsonResponse

def home(request):
    qs = Product.objects.all()
    serialized_data = serialize("json", qs)
    serialized_data = json.loads(serialized_data)
    return JsonResponse(serialized_data, status=200)
