from django.shortcuts import render
from django.http import HttpResponse
from example_app.tasks import send_email_task, sleepy

# def index(request):
#     sleepy.delay(10)
#     print(f'view.index: sleepy.delay')
#     return HttpResponse('<h1>Task is Done!</h1>')

# def index(request):
#     send_email_task()
#     print(f'view.index: send_email_task')
#     return HttpResponse('<h1>Email has been sent!</h1>')

def index(request):
    send_email_task.delay()
    print(f'view.index: send_email_task_celery')
    return HttpResponse('<h1>Email has been sent by celery!</h1>')