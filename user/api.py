from django.shortcuts import render, HttpResponse

from my_celery.sms.tasks import send_verify_code

# Create your views here.
def send_sms_vcode(request):
    # 异步任务
    phonenum = request.POST.get('phonenum')
    phonenum = 13887808102
    send_verify_code.delay(phonenum)
    return HttpResponse('OK')

    # 定时任务
    from datetime import datetime, timedelta
    ctime = datetime.now()
    # 默认用utc时间
    utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
    time_delay = timedelta(seconds=10)
    task_time = utc_ctime + time_delay
    result = send_verify_code.apply_async([phonenum, ], eta=task_time)
    print(result.id)
    return HttpResponse('OK')


def register(request):
    pass