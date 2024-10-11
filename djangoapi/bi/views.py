import traceback, requests, os
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from utils.customclass import SuccessResponse, PeiDiError, ExceptionResponse, PeiDiErrorResponse
from utils.util import get_mysql_process_response_with_redis, call_db_procedure, call_proc_and_write_cache

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

def read_from_db_write_to_cache(proc_name, parameters_list):
    redis_key = '{}#{}'.format(proc_name, "/".join(parameters_list))
    result = call_proc_and_write_cache(
        key=redis_key,
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

        # SPU日销额
        for d in get_dates_until_yesterday():
            read_from_cache_or_db(proc_name='CalculateSPUPerformance', parameters_list=[d + ' 00:00:00', d + ' 23:59:59'])

        channels = read_from_cache_or_db(proc_name='GetSalesAmountRanking', parameters_list=['2024-01-01 00:00:00', '2024-01-31 23:59:59'])
        for row in channels:
            for m in month_ranges_until_now:
                read_from_cache_or_db(proc_name='GetSalesAmountRankingByChannel', parameters_list=[row[0], m[0] + ' 00:00:00', m[1] + ' 23:59:59'])
            
        result = read_from_cache_or_db(proc_name='CalculateSPUPerformance', parameters_list=['2024-01-01 00:00:00', '2024-01-31 23:59:59'])
        for row in result:
            read_from_cache_or_db(proc_name='CalculateShopBySPU', parameters_list=[row[0], year_start, end])
            for m in month_ranges_until_now:
                read_from_cache_or_db(proc_name='CalculateShopBySPU', parameters_list=[row[0], m[0] + ' 00:00:00', m[1] + ' 23:59:59'])
            
            # SPU各店铺的日销额
            for d in get_dates_until_yesterday():
                read_from_cache_or_db(proc_name='CalculateShopBySPU', parameters_list=[row[0], d + ' 00:00:00', d + ' 23:59:59'])

        return SuccessResponse(result)
    except Exception:
        return ExceptionResponse(traceback.format_exc().split('\n')[-2])

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_increment_data(request):
    try:
        month_ranges_until_now = get_month_ranges_until_now()
        m = month_ranges_until_now[0]
        print('当前月起始日期', m)

        read_from_db_write_to_cache('GetSalesAmountRanking', parameters_list=[m[0] + ' 00:00:00', m[1] + ' 23:59:59'])
        read_from_db_write_to_cache('CalculateSPUPerformance', parameters_list=[m[0] + ' 00:00:00', m[1] + ' 23:59:59'])

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
            read_from_db_write_to_cache(proc_name=proc['name'], parameters_list=proc['args'])

        all_dates = get_dates_until_yesterday()
        d = all_dates[-1]
        print('昨天的时期是', d)

        read_from_db_write_to_cache(proc_name='CalculateSPUPerformance', parameters_list=[d + ' 00:00:00', d + ' 23:59:59'])

        channels = read_from_cache_or_db(proc_name='GetSalesAmountRanking', parameters_list=['2024-01-01 00:00:00', '2024-01-31 23:59:59'])
        for row in channels:
            read_from_db_write_to_cache(proc_name='GetSalesAmountRankingByChannel', parameters_list=[row[0], m[0] + ' 00:00:00', m[1] + ' 23:59:59'])
            
        result = read_from_cache_or_db(proc_name='CalculateSPUPerformance', parameters_list=['2024-01-01 00:00:00', '2024-01-31 23:59:59'])
        for row in result:
            read_from_db_write_to_cache(proc_name='CalculateShopBySPU', parameters_list=[row[0], year_start, end])
            read_from_db_write_to_cache(proc_name='CalculateShopBySPU', parameters_list=[row[0], m[0] + ' 00:00:00', m[1] + ' 23:59:59'])
            read_from_db_write_to_cache(proc_name='CalculateShopBySPU', parameters_list=[row[0], d + ' 00:00:00', d + ' 23:59:59'])

        return SuccessResponse(result)
    except Exception:
        return ExceptionResponse(traceback.format_exc().split('\n')[-2])

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def generate_spu_sales_data(request):
    base_url = 'http://localhost:8000'
    auth_token = os.environ.get('DJANGO_AUTH_TOKEN')
    
    # 定义 API 地址和请求头
    API_URL = base_url + "/bi/call-proc"
    HEADERS = {
        "Authorization": f"Token {auth_token}",
        "Content-Type": "application/json"
    }

    # 获取昨天的日期
    yesterday = datetime.now() - timedelta(days=1)
    start_time = yesterday.replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
    end_time = yesterday.replace(hour=23, minute=59, second=59, microsecond=999999).isoformat()

    # 定义请求的数据
    payload = {
        "name": "CalculateSPUPerformance",
        "params": [
            start_time,
            end_time
        ],
        "flush": True
    }

    # 定义需要匹配的产品名称
    product_names = [
        "鸭肉干", "鸡肉干", "薄脆鸡肉", "鲭鱼干", "姜黄鸡", "鸡肉紫薯",
        "鸭肉红薯", "鸡肉胡萝卜", "鸡肉香蕉", "鸡肉苹果", "鸭肉梨",
        "冻干兔耳朵", "冻干原切猪心", "冻干牛肝酥", "爵宴组合装", "爵宴礼盒",
        "爵宴风干粮", "狗罐", "新西兰牛草胃", "新西兰鹿肺块", "新西兰羊肝块",
        "smb其他", "编织球 & 功能卷", "缠肉卷棒", "夹心", "迷你洁齿骨",
        "小中大号洁齿骨", "发泡棒", "迷你洁齿骨大礼包", "趣玩洁齿大礼包",
        "一口好牙大礼包", "ok结骨", "成犬洁齿骨", "齿能其他", "健齿环",
        "经典洁骨", "98K主食罐", "好适嘉鲜肉烘焙粮", "牛肉粒", "好适嘉狗罐头",
        "鲭鱼罐", "黄金罐", "成长罐", "begogo鸡肉冻干", "好适嘉其他",
        "彩虹食谱犬粮", "好适嘉护理粮", "猫砂", "猫酱其他", "彩虹食谱猫粮",
        "begogo其他"
    ]

    # 发送 POST 请求获取数据
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    
    # 处理 API 响应
    if response.status_code == 200:
        data = response.json()
        api_result = data.get("result", [])
        api_map = {item[0]: item[1] for item in api_result}  # 创建字典以便快速查找
    
        # 准备输出数据
        output_data = []
        for name in product_names:
            value = api_map.get(name, None)  # 获取对应的值，如果没有则为 None
            output_data.append([name, value])  # 将产品名称和对应的值添加到输出数据中
    
        # 创建 DataFrame 并保存为 Excel
        df = pd.DataFrame(output_data, columns=["产品名称", "接口数据"])
        df.to_excel("SPU日销售额" + start_time[:10] + ".xlsx", index=False)
    
        print("Excel 文件已生成：产品数据.xlsx")
        return SuccessResponse('Excel文件已生成')
    else:
        print(f"请求失败，状态码：{response.status_code}，消息：{response.text}")
        return SuccessResponse('Excel文件生成失败')
