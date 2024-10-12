import traceback, requests, os, oss2
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
    # Step 1: 调用 API 获取数据
    yesterday_start = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d 00:00:00')
    yesterday_end = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d 23:59:59')
    
    base_url = "http://localhost:8000"
    auth_token = os.environ.get('DJANGO_AUTH_TOKEN')
    url = base_url + "/bi/call-proc"
    headers = {
        "Authorization": f"Token {auth_token}",
        "Content-Type": "application/json"
    }
    data = {
        "name": "CalculateSPUPerformance",
        "params": [yesterday_start, yesterday_end],
        "flush": True
    }
    
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    
    # Step 2: 处理 API 返回的数据
    result = response_data.get("result", [])
    names_to_match = [
        "鸭肉干", "鸡肉干", "薄脆鸡肉", "鲭鱼干", "姜黄鸡", "鸡肉紫薯", "鸭肉红薯", "鸡肉胡萝卜", "鸡肉香蕉", 
        "鸡肉苹果", "鸭肉梨", "冻干兔耳朵", "冻干原切猪心", "冻干牛肝酥", "爵宴组合装", "爵宴礼盒", 
        "爵宴风干粮", "狗罐", "新西兰牛草胃", "新西兰鹿肺块", "新西兰羊肝块", "smb其他", "编织球 & 功能卷", 
        "缠肉卷棒", "夹心", "迷你洁齿骨", "小中大号洁齿骨", "发泡棒", "迷你洁齿骨大礼包", "趣玩洁齿大礼包", 
        "一口好牙大礼包", "ok结骨", "成犬洁齿骨", "齿能其他", "健齿环", "经典洁骨", "98K主食罐", 
        "好适嘉鲜肉烘焙粮", "牛肉粒", "好适嘉狗罐头", "鲭鱼罐", "黄金罐", "成长罐", "begogo鸡肉冻干", 
        "好适嘉其他", "彩虹食谱犬粮", "好适嘉护理粮", "猫砂", "猫酱其他", "彩虹食谱猫粮", "begogo其他"
    ]
    
    # 生成匹配结果
    matched_data = []
    for name in names_to_match:
        found = False
        for item in result:
            if item[0] == name:
                matched_data.append([name, item[1]])
                found = True
                break
        if not found:
            matched_data.append([name, None])
    
    # Step 3: 将数据保存为 Excel 文件
    df = pd.DataFrame(matched_data, columns=["SPU", "销售额"])
    file_name = f'{yesterday_start[:10]}.xlsx'.replace('-', '')
    df.to_excel(file_name, index=False)
    
    # Step 4: 上传到阿里云 OSS
    oss_endpoint = os.environ.get('OSS_ENDPOINT')
    oss_accessKeyId = os.environ.get('OSS_ACCESS_KEY_ID')
    oss_accessKeySecret = os.environ.get('OSS_ACCESS_KEY_SECRET')
    oss_bucketName = os.environ.get('OSS_BUCKET_NAME')
    
    # 创建OSS客户端
    auth = oss2.Auth(oss_accessKeyId, oss_accessKeySecret)
    bucket = oss2.Bucket(auth, oss_endpoint, oss_bucketName)
    
    # 上传文件
    oss_file_name = f'{file_name}'
    bucket.put_object_from_file(oss_file_name, file_name)
    
    # 获取文件的访问URL
    file_url = f'https://{oss_bucketName}.oss-cn-hangzhou.aliyuncs.com/{oss_file_name}'
    print(f'文件上传成功，访问地址为: {file_url}')
    return SuccessResponse({ "file_name": file_name, "file_url": file_url })
    