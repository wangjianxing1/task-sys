"""
第三方配置
"""
# 互亿无限短信配置 根据世纪进行修改
from local_settings import HYWX_ACCOUNT, HYWX_PASSWORD

HY_SMS_URL = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'
HY_SMS_PARAMS = {
    'account': HYWX_ACCOUNT,
    'password': HYWX_PASSWORD,
    'content': '您的验证码是：%s。请不要把验证码泄露给其他人。',
    'mobile': None,
    'format': 'json'
}
