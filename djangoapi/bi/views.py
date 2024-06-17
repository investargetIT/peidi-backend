from django.db import connection

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from utils.customclass import SuccessResponse, PeiDiError, ExceptionResponse, PeiDiErrorResponse


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_sales_amount_ranking(request):
    date_start = request.data.get('start_date')
    date_end = request.data.get('end_date')
    print(date_start, date_end)

    result = []
    with connection.cursor() as cursor:
        time_start = date_start + ' 00:00:00'
        time_end = date_end + ' 23:59:59'
        cursor.callproc('GetSalesAmountRanking', (time_start, time_end))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            r = {
                "channel": row[0],
                "shop_name": row[1],
                "goods_name": row[2],
                "sales_amount": float(row[3])
            }
            print(r)
            result.append(r)

    return SuccessResponse(result)
