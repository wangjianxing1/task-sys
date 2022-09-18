from django.shortcuts import render, HttpResponse

from my_celery.sms.tasks import send_verify_code

import json


# Create your views here.
def send_sms_vcode(request):
    # 异步任务
    phonenum = request.POST.get('phonenum')
    from task_sys.settings import DEBUG
    if DEBUG == False:
        send_verify_code.delay(phonenum)
    else:
        from django.core.cache import caches
        key = 'VerifyCode-%s' % phonenum
        caches['verify'].set(key, 1234567, 120)  # 120秒后过期
    data = json.dumps({'code': 200, 'message': 'ok'})
    return HttpResponse(data)

    # # 定时任务
    # from datetime import datetime, timedelta
    # ctime = datetime.now()
    # # 默认用utc时间
    # utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
    # time_delay = timedelta(seconds=10)
    # task_time = utc_ctime + time_delay
    # result = send_verify_code.apply_async([phonenum, ], eta=task_time)
    # print(result.id)
    # return HttpResponse('OK')


from django import forms
from user import models
from django.core.validators import RegexValidator #正则匹配
from django.core.exceptions import ValidationError


class RegisterModelForm(forms.ModelForm):
    mobile_phone = forms.CharField(label='手机号',
                                   validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机格式错误')])
    password = forms.CharField(label='输入密码', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '请输入密码'}))
    confirm_password = forms.CharField(label='确认密码', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '请确认密码'}))
    code = forms.CharField(label='验证码', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '请输入验证码'}))

    class Meta:
        model = models.UserInfo
        # fields = "__all__"
        fields = ['username', 'email', 'password',
                  'confirm_password', 'mobile_phone', 'code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入%s' % (field.label)


def register(request):
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})
