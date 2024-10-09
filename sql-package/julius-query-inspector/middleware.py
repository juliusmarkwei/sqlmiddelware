from decimal import Decimal
from django.conf import settings
from django.db import connection
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from sqlparse import format


def new_middleware(get_response):
    def middleware(request):
        response = get_response(request)

        if settings.DEBUG:
            numQueries = len(connection.queries)
            totalExecutionTime = Decimal()
            checkDuplicates = set()

            for query in connection.queries:
                totalExecutionTime += Decimal(query["time"])
                checkDuplicates.add(str(query["sql"]))
                sqlFormatted = format(str(query["sql"]), reindent=True)
                print(highlight(sqlFormatted, SqlLexer(), TerminalFormatter()))

            print("-------------------------------------")
            print("[SQL Stats]")
            print(f"Number of queries: {numQueries}")
            print(f"Duplicate queries: {len(connection.queries) - len(checkDuplicates)}")
            print(f"Total execution time: {totalExecutionTime} seconds")
            print("-------------------------------------")

        return response

    return middleware
