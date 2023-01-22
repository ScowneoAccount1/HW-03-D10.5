import os
from celery import Celery
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')
 
app = Celery('NewsPotal')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send_news_every_monday': {
        'task': 'news.tasks.complete_order', #! replace COMPELTE with an actial function from news.tasks
        'schedule': crontab(day_of_week='monday', hour='8'),
    },
}