from django.shortcuts import render
from django.http import HttpResponse
import time

from celery import shared_task

@shared_task
def my_task():
    time.sleep(10)
    open('output_ibe_one.txt', 'w').close()

def home(request):
    print(my_task)
    my_task.delay()
    return HttpResponse("Hello, world! This is the home page.")


def test_view(request):
    return HttpResponse('This is a test view. It should not be cached.')