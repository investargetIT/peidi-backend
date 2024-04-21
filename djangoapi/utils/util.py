#记录request error
import datetime
import traceback

from django.core.cache import cache

APILOG_PATH = {}

def catchexcption(request):
    now = datetime.datetime.now()
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    filepath = APILOG_PATH['excptionlogpath'] + '/' + now.strftime('%Y-%m-%d')
    f = open(filepath, 'a')
    f.writelines(now.strftime('%H:%M:%S') + '\n'
                 '请求用户ip:%s' % ip + '\n'
                 'user_agent:'+ request.META['HTTP_USER_AGENT']+ '\n'
                 '请求发起用户id:'+str(request.user.id)+ '\n'
                 'path: '+request.path + 'method:' + request.method +'\n'+
                 traceback.format_exc() + '\n\n\n\n')
    f.close()


def read_from_cache(key):
    value = cache.get(key.encode('utf-8'))
    return value
#写
def write_to_cache(key, value, time_out=3600):
    cache.set(key.encode('utf-8'), value, time_out)

def cache_delete_key(key):
    cache.delete(key.encode('utf-8'))