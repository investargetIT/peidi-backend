from django.urls import path
from . import views

dingTalkapi = views.DingTalkIMRobot.as_view({
    'post': 'test_add_task',
})

urlpatterns = [
    path("dingtalk", dingTalkapi, name="dingTalkapi"),
]
