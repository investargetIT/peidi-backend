import traceback
from django.db import connection

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from utils.customclass import SuccessResponse, PeiDiError, ExceptionResponse, PeiDiErrorResponse


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def call_procedure(request):
    try:
        name = request.query_params.get('name')
        parameters_list = request.data

        with connection.cursor() as cursor:
            result = []
            cursor.callproc(name, tuple(parameters_list))
            rows = cursor.fetchall()
            for row in rows:
                result.append(row)
            return SuccessResponse(result)
        
    except Exception:
        return ExceptionResponse(traceback.format_exc().split('\n')[-2])
