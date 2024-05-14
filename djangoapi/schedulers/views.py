import os, json, requests

from rest_framework import viewsets
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from utils.customclass import SuccessResponse, PeiDiError, ExceptionResponse, PeiDiErrorResponse
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger

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
    response = requests.post(url, data=data).content
    res = json.loads(response.decode())
    print(res)
    errcode = res.get('errcode')
    if errcode != 0:
        raise PeiDiError(20501, msg=res['errmsg'])
    return res['result']['userid']

class DingTalkIMRobot(viewsets.ModelViewSet):

    # 与前端的接口
    def test_add_task(self, request):
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
                id='job_name',
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
