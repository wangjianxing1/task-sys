# 创建celery异步对象
import os
from celery import Celery

"""“
”独立”Django使用需要调用django.setup()
这个’独立‘的意思就是，运行一个python脚本运行，
但是这个脚本是需要依赖django中的一些配置，
那么就需要用到django.setup()；
"""
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_sys.settings')
django.setup()
django.setup()



app = Celery('task-sys')



app.config_from_object('my_celery.config')

app.autodiscover_tasks(['my_celery.sms',])

# 启动Celery的命令
# 强烈建议切换目录到 my_celery根目录下启动
# celery -A my_celery.main worker --loglevel=info