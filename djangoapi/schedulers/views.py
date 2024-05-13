import json
from django.http import JsonResponse
from rest_framework import viewsets
from apscheduler.schedulers.blocking import BlockingScheduler
from django_apscheduler.jobstores import DjangoJobStore
from utils.customclass import SuccessResponse
from django.conf import settings
from schedulers.management.commands.runapscheduler import scheduler
from apscheduler.triggers.cron import CronTrigger

class DingTalkIMRobot(viewsets.ModelViewSet):



    # 与前端的接口
    def test_add_task(self, request, *args, **kwargs):

        # 具体要执行的代码
        def test():
            f = open("/code/utils/demo.txt", "a")
            f.write("Now the file has more content!\n")
            f.close()
            pass

        # scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        # scheduler.add_jobstore(DjangoJobStore(), "default")
        # content = json.loads(request.body.decode())  # 接收参数
        try:
            # start_time = content['start_time']  # 用户输入的任务开始时间, '10:00:00'
            # start_time = start_time.split(':')
            # hour = int(start_time)[0]
            # minute = int(start_time)[1]
            # second = int(start_time)[2]
            # s = content['s']  # 接收执行任务的各种参数
            
            # 创建任务
            # scheduler.add_job(test, 'cron', hour=hour, minute=minute, second=second, args=[s])
            print(scheduler)
            scheduler.add_job(
                test,
                trigger=CronTrigger(second="*/10"),  # Every 10 seconds
                id="my_job1",  # The `id` assigned to each job MUST be unique
                max_instances=1,
                replace_existing=True,
            )
            
            code = '200'
            message = 'success'
        except Exception as e:
            print(e)
            code = '400'
            message = e
            
        back = {
            'code': code,
            'message': message
        }
        # return JsonResponse(json.dumps(back, ensure_ascii=False), safe=False)
        return SuccessResponse({'count': 0, 'data': []})
        

