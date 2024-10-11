#记录request error
import datetime
import traceback
from django.db import connection
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

def getMysqlProcessResponseWithRedis(redis_key, proc_name, args):
    res_data = read_from_cache(redis_key)
    if not res_data:
        with connection.cursor() as cursor:
            cursor.callproc(proc_name, args)
            row = cursor.fetchall()
            res_data = str(row)
            write_to_cache(redis_key, res_data)
    return res_data

def call_db_procedure(proc_name, args):
    res_data = []
    with connection.cursor() as cursor:
        cursor.callproc(proc_name, args)
        rows = cursor.fetchall()
        for row in rows:
            res_data.append(row)
    return res_data

def get_mysql_process_response_with_redis(redis_key, proc_name, args):
    res_data = read_from_cache(redis_key)
    if not res_data:
        res_data = call_db_procedure(proc_name, args)
        write_to_cache(redis_key, res_data, time_out=None)
    return res_data

def call_proc_and_write_cache(key, proc_name, args):
    data = call_db_procedure(proc_name, args)
    write_to_cache(key, data, time_out=None)
