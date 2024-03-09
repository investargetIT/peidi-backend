#记录request error
import datetime
import traceback

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