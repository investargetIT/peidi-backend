import binascii
import datetime
import os
import random

from django.db import models

# Create your models here.
class MobileAuthCode(models.Model):
    ip = models.CharField(max_length=40, blank=True, null=True, verbose_name='请求验证码ip')
    areacode = models.CharField(max_length=8, blank=True, default='86')
    mobile = models.CharField(help_text='手机号', max_length=32)
    sms_token = models.CharField(help_text='验证码token', max_length=32)
    sms_code = models.CharField(help_text='验证码', max_length=32)
    createTime = models.DateTimeField(blank=True, null=True)
    is_used = models.BooleanField(blank=True, default=False, verbose_name='验证码是否已被使用')
    def isexpired(self):
        return datetime.datetime.now() - self.createTime >= datetime.timedelta(minutes=5)
    def __str__(self):
        return self.sms_code
    class Meta:
        db_table = "mobileAuthCode"
    def save(self, *args, **kwargs):
        if not self.sms_token:
            self.sms_token = binascii.hexlify(os.urandom(16)).decode()
        if not self.sms_code:
            self.sms_code = self.getRandomCode()
        if not self.pk:
            self.createTime = datetime.datetime.now()
        return super(MobileAuthCode, self).save(*args, **kwargs)
    def getRandomCode(self):
        code_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        myslice = random.sample(code_list, 6)
        code = ''.join(str(i) for i in myslice)
        return code