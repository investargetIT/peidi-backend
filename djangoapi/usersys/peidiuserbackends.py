from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password

from utils.customclass import PeiDiError

UserModel = get_user_model()
class PeidiUserBackend(ModelBackend):
    def authenticate(self, request, mobile=None, password=None, **kwargs):
        try:
            if mobile is None or password is None:
                return None
            raw_mobile = make_password(mobile)
            user = UserModel.objects.get(mobile=raw_mobile)
        except UserModel.DoesNotExist:
            raise PeiDiError(code=2002, msg='用户不存在')
        except Exception as err:
            raise PeiDiError(code=9999, msg='UserBackend/authenticate验证失败\n,%s' % err)
        else:
            if user.check_password(password):
                return user
        return None
