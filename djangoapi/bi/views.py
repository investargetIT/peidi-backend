import traceback
from django.db import connection

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from utils.customclass import SuccessResponse, PeiDiError, ExceptionResponse, PeiDiErrorResponse
from utils.util import get_mysql_process_response_with_redis, call_db_procedure


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def call_procedure(request):
    try:
        proc_name = request.data.get('name')
        parameters_list = request.data.get('params')
        flush = request.data.get('flush')
        
        result = []
        if flush:
            result = call_db_procedure(
                proc_name=proc_name,
                args=tuple(parameters_list)
            )
        else:
            redis_key = '{}#{}'.format(proc_name, "/".join(parameters_list))
            result = get_mysql_process_response_with_redis(
                redis_key=redis_key,
                proc_name=proc_name,
                args=tuple(parameters_list)
            )

        return SuccessResponse(result)
        
    except Exception:
        return ExceptionResponse(traceback.format_exc().split('\n')[-2])
