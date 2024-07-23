import os, json, requests, logging
from datetime import datetime, timedelta

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger

from django_apscheduler.jobstores import DjangoJobStore

from utils.customclass import SuccessResponse, PeiDiError, ExceptionResponse, PeiDiErrorResponse
from utils.util import get_mysql_process_response_with_redis

logger = logging.getLogger('django')

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")
scheduler.start()

# 具体要执行的代码
def test():
    f = open("/code/utils/demo.txt", "a")
    f.write("Now the file has more content!\n")
    f.close()
    pass

def test1(content):
    f = open("/code/utils/demo1.txt", "w")
    f.write(content)
    f.close()
    pass

def test2(content):
    f = open("/code/utils/demo2.txt", "w")
    f.write(content)
    f.close()
    pass

def send_dingtalk_msg(content, mobiles):
    url = os.environ.get('DINGTALK_IMROBOT_WEBHOOK')
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
	        "atMobiles": mobiles.split(',')
        }
    }
    response = requests.post(url, json=data).content
    res = json.loads(response.decode())
    print(res)
    errcode = res.get('errcode')
    if errcode != 0:
        raise PeiDiError(20501, msg=res['errmsg'])
    
def read_from_cache_or_db(proc_name, parameters_list):
    redis_key = '{}#{}'.format(proc_name, "/".join(parameters_list))
    result = get_mysql_process_response_with_redis(
        redis_key=redis_key,
        proc_name=proc_name,
        args=tuple(parameters_list)
    )
    logger.info(result)

def get_dashboard_data():
    yesterday = datetime.now() - timedelta(1)
    yesterday_str = datetime.strftime(yesterday, '%Y-%m-%d')
    yesterday_month = datetime.strftime(yesterday, '%Y-%m')
    start = yesterday_month + '-01 00:00:00'
    end = yesterday_str + ' 23:59:59'
    # TODO
    for name in []:
        read_from_cache_or_db(proc_name=name, parameters_list=[start, end])
    pass

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def schedule_send_dingtalk_msg(request):
    job_id = request.data.get('job_id')
    content = request.data.get('content')
    at_mobiles = request.data.get('at_mobiles')
    scheduled_time = request.data.get('scheduled_time')
        
    # scheduler.add_job(
    #     test,
    #     trigger=CronTrigger(second="*/10"),  # Every 10 seconds
    #     id="my_job1",  # The `id` assigned to each job MUST be unique
    #     max_instances=1,
    #     replace_existing=True,
    # )

    if scheduled_time:
        scheduler.add_job(
            send_dingtalk_msg,
            trigger=DateTrigger(scheduled_time),
            id=job_id,
            args=[content, at_mobiles],
            max_instances=1,
            replace_existing=True,
        )
    else:
        scheduler.add_job(
            send_dingtalk_msg,
            args=[content, at_mobiles],
            max_instances=1,
            replace_existing=True,
        )

    return SuccessResponse('定时任务创建成功')

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def schedule_get_dashboard_data(request):
    
    scheduler.add_job(
        get_dashboard_data,
        trigger=CronTrigger(day="*", hour=0),
        id="get_dashboard_data",
        max_instances=1,
        replace_existing=True,
    )

    return SuccessResponse('定时任务创建成功')
