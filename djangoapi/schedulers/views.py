import json
from django.http import JsonResponse
from rest_framework import viewsets
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from utils.customclass import SuccessResponse
from apscheduler.triggers.cron import CronTrigger

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")
scheduler.start()

# 具体要执行的代码
def test():
    f = open("/code/utils/demo.txt", "a")
    f.write("Now the file has more content!\n")
    f.close()
    pass

class DingTalkIMRobot(viewsets.ModelViewSet):

    # 与前端的接口
    def test_add_task(self, request, *args, **kwargs):
        try:
            # 创建任务
            # scheduler.add_job(test, 'cron', hour=hour, minute=minute, second=second, args=[s])
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
        

