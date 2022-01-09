from celery import shared_task
from time import sleep
from django.core.mail import send_mail
@shared_task
def sleepy(duration):
    sleep(duration)
    print(f'sleep-duration: {duration}')

@shared_task
def send_email_task():
    sleep(10)
    send_mail(
        subject='Celery Task Worked!',
        message='This is proof the task worded!',
        from_email='server8email@gmail.com',
        recipient_list=['lixwov@gmail.com','l.ixwov@gmail.com','lixwo.v@gmail.com'],
        fail_silently=False,
    )
