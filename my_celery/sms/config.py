# 发送短信配置文件

"""
第三方配置
"""
# 互亿无限短信配置 根据实际进行修改
# 短信配置
# 互亿无限短信配置
HYWX_ACCOUNT = 'C468545028'
HYWX_PASSWORD = '60c5157972c733cae505ff4e71f6922e'

HY_SMS_URL = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'
HY_SMS_PARAMS = {
    'account': HYWX_ACCOUNT,
    'password': HYWX_PASSWORD,
    'content': '您的验证码是：%s。请不要把验证码泄露给其他人。',
    'mobile': None,
    'format': 'json'
}
