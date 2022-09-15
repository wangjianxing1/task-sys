# 创建短信异步任务

import random
import time
import requests

import json

from django.core.cache import cache

from my_celery.main import app
# from my_celery.sms import config
from . import config



def gen_verify_code(length=6):
    return random.randrange(10 ** (length - 1), 10 ** length)

@app.task
def send_verify_code(phonenum):
    vcode = gen_verify_code()
    key = 'VerifyCode-%s' % phonenum
    cache.set(key, vcode, 120)  # 120秒后过期
    sms_cfg = config.HY_SMS_PARAMS.copy()
    sms_cfg['content'] = sms_cfg['content'] % vcode
    sms_cfg['mobile'] = phonenum
    print(type(phonenum), phonenum)
    print(vcode)
    response = requests.post(config.HY_SMS_URL, data=sms_cfg)
    return response
