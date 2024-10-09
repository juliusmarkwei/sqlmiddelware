from django.core.serializers import serialize
from django.db import connection
from .models import Product
import json
from django.http import JsonResponse
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from sqlparse import format

def home(request):
    qs = Product.objects.all()
    serialized_data = serialize("json", qs)

    queries = list(connection.queries)
    for query in queries:
        sqlFormatted = format(str(query["sql"]), reindent=True)
        print(highlight(sqlFormatted, SqlLexer(), TerminalFormatter()))

    serialized_data = json.loads(serialized_data)
    return JsonResponse(serialized_data, safe=False, status=200)
