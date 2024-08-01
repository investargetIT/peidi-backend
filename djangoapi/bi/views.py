import traceback
from datetime import datetime, timedelta

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
    
def read_from_cache_or_db(proc_name, parameters_list):
    redis_key = '{}#{}'.format(proc_name, "/".join(parameters_list))
    result = get_mysql_process_response_with_redis(
        redis_key=redis_key,
        proc_name=proc_name,
        args=tuple(parameters_list)
    )
    return result

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_dashboard_data(request):
    try:
        yesterday = datetime.now() - timedelta(1)
        thirtydays_ago = yesterday - timedelta(30)
        yesterday_str = datetime.strftime(yesterday, '%Y-%m-%d')
        thirtydays_ago_str = datetime.strftime(thirtydays_ago, '%Y-%m-%d')
        yesterday_year = datetime.strftime(yesterday, '%Y')
        yesterday_month = datetime.strftime(yesterday, '%Y-%m')
        year_start = yesterday_year + '-01-01 00:00:00'
        month_start = yesterday_month + '-01 00:00:00'
        thirtydays_ago_start = thirtydays_ago_str + ' 00:00:00'
        end = yesterday_str + ' 23:59:59'
        proc_list = [
            { 'name': 'GetSalesAmountRanking', 'args': [month_start, end] },
            { 'name': 'CalculateSPUPerformance', 'args': [month_start, end] },
            { 'name': 'CalculateSPUPerformance', 'args': [year_start, end] },
            { 'name': 'GetOrderCountByCity', 'args': [year_start, end] },
            { 'name': 'GetOrderCountByCity', 'args': [thirtydays_ago_start, end] },
        ]
        for proc in proc_list:
            read_from_cache_or_db(proc_name=proc['name'], parameters_list=proc['args'])

        result = read_from_cache_or_db(proc_name='CalculateSPUPerformance', parameters_list=['2024-01-01 00:00:00', '2024-01-31 23:59:59'])
        for row in result:
            read_from_cache_or_db(proc_name='CalculateShopBySPU', parameters_list=[row[0], year_start, end])
        return SuccessResponse(result)
    except Exception:
        return ExceptionResponse(traceback.format_exc().split('\n')[-2])
    