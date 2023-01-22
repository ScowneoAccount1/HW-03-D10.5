from signals.py import save_posts

from celery import shared_task
import time
from .models import Post


@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")


@shared_task
def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i+1)


@shared_task
def complete_order(oid):
    id = oid # эта переменная уже не нужна. но я оставил какойто код с ней, чтобы можно было легче копирывать код
    
    subscribers_list = [user.email for user in category.subscr_user.all()]

    msg = EmailMultiAlternatives(subject,
                                         body=f'В категориях, на которые вы подписаны появилась новая статья: \n\n'
                                              f'Ссылка: http://127.0.0.1:8000/news/{post.id} \n\n'
                                              f'Заголовок: {post.heading}\n'
                                              f'Превью: {post.preview()}\n',
                                         from_email=settings.EMAIL_FROM,
                                         to=subscribers_list)

    msg.send()

    


# @shared_task
# def send_latest_news():
#     post = Post.objects.get()
#     post.save()