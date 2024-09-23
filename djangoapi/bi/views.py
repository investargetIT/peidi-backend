import traceback
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

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

def get_month_ranges_until_now():
    now = datetime.now()
    yesterday = now - timedelta(days=1)
    month_ranges = []
    
    for i in range(yesterday.month):
        start_date = (yesterday - relativedelta(months=i)).replace(day=1)
        if i == 0:  # 当前月
            end_date = yesterday
        else:
            end_date = (start_date + relativedelta(months=1)) - timedelta(days=1)
        
        month_ranges.append((start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")))
    
    return month_ranges

# 获取自2024年1月1日起截止到昨日的所有日期
def get_dates_until_yesterday():
    # 设置起始日期
    start_date = datetime(2024, 1, 1)
    # 获取昨天的日期
    end_date = datetime.now() - timedelta(days=1)
    
    # 初始化日期列表
    date_list = []
    
    # 生成日期列表
    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    
    return date_list

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_dashboard_data(request):
    try:
        month_ranges_until_now = get_month_ranges_until_now()
        print(month_ranges_until_now)

        for m in month_ranges_until_now:
            read_from_cache_or_db('GetSalesAmountRanking', parameters_list=[m[0] + ' 00:00:00', m[1] + ' 23:59:59'])
            read_from_cache_or_db('CalculateSPUPerformance', parameters_list=[m[0] + ' 00:00:00', m[1] + ' 23:59:59'])

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
            { 'name': 'CalculateSPUPerformance', 'args': [year_start, end] },
            { 'name': 'GetOrderCountByCity', 'args': [year_start, end] },
            { 'name': 'GetOrderCountByCity', 'args': [thirtydays_ago_start, end] },
        ]
        for proc in proc_list:
            read_from_cache_or_db(proc_name=proc['name'], parameters_list=proc['args'])

        channels = read_from_cache_or_db(proc_name='GetSalesAmountRanking', parameters_list=['2024-01-01 00:00:00', '2024-01-31 23:59:59'])
        for row in channels:
            for m in month_ranges_until_now:
                read_from_cache_or_db(proc_name='GetSalesAmountRankingByChannel', parameters_list=[row[0], m[0] + ' 00:00:00', m[1] + ' 23:59:59'])
            
        result = read_from_cache_or_db(proc_name='CalculateSPUPerformance', parameters_list=['2024-01-01 00:00:00', '2024-01-31 23:59:59'])
        for row in result:
            read_from_cache_or_db(proc_name='CalculateShopBySPU', parameters_list=[row[0], year_start, end])
            for m in month_ranges_until_now:
                read_from_cache_or_db(proc_name='CalculateShopBySPU', parameters_list=[row[0], m[0] + ' 00:00:00', m[1] + ' 23:59:59'])
            
            # # SPU各店铺的日销量
            # for d in get_dates_until_yesterday():
            #     read_from_cache_or_db(proc_name='CalculateShopBySPU', parameters_list=[row[0], d + ' 00:00:00', d + ' 23:59:59'])
        
        # SPU日销量
        for d in get_dates_until_yesterday():
            read_from_cache_or_db(proc_name='CalculateSPUPerformance', parameters_list=[d + ' 00:00:00', d + ' 23:59:59'])

        return SuccessResponse(result)
    except Exception:
        return ExceptionResponse(traceback.format_exc().split('\n')[-2])
    