from django.contrib.auth import password_validation
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import (
    check_password, make_password,
)
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from djangoapi.utils.customclass import PeiDiError


class PeidiUserBackend(ModelBackend):
    def authenticate(self, request, mobile=None, password=None, **kwargs):
        try:
            if mobile is None or password is None:
                return None
            raw_mobile = make_password(mobile)
            user = PeidiUser.objects.get(mobile=raw_mobile)
        except PeidiUser.DoesNotExist:
            raise PeiDiError(code=2002, msg='用户不存在')
        except Exception as err:
            raise PeiDiError(code=9999, msg='UserBackend/authenticate验证失败\n,%s' % err)
        else:
            if user.check_password(password):
                return user
        return None

class PeidiUserManager(BaseUserManager):
    def create_user(self, username, mobile=None, password=None, **extra_fields):
        user = self.model(username=username, is_superuser=False, **extra_fields)
        user.set_mobile(mobile)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, mobile, password):
        user = self.create_user(username, mobile, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class PeidiUser(AbstractUser):
    """自定义用户模型类"""
    username_validator = UnicodeUsernameValidator()
    id = models.AutoField(primary_key=True)
    username = models.CharField(_("username"), max_length=128, unique=True, help_text=_(
            "Required. 128 characters or fewer. Letters, digits and @/./+/-/_ only."
        ), validators=[username_validator]
    )
    mobile = models.CharField(max_length=128, unique=True, verbose_name='手机号')
    email = models.EmailField(_("email address"), blank=True)
    address = models.TextField(_("address"), max_length=200, blank=True)
    objects = PeidiUserManager()
    REQUIRED_FIELDS = ["mobile"]
    _mobile = None
    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def set_mobile(self, raw_mobile):
        self.mobile = make_password(raw_mobile)
        self._mobile = raw_mobile

    def check_mobile(self, raw_mobile):
        def setter(raw_mobile):
            self.set_mobile(raw_mobile)
            self._mobile = None
            self.save(update_fields=["mobile"])
        return check_password(raw_mobile, self.mobile, setter)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None

    def __str__(self):
        return self.username