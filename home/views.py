from django.shortcuts import render
from django.http import HttpResponse
import time

from celery import shared_task

from core.loguru_logger import logger

@shared_task
def my_task():
    logger.info("my_task started.")
    time.sleep(10)
    open('output_ibe_one.txt', 'w').close()
    logger.success("my_task completed and file created.")

def home(request):
    logger.info("home view accessed by user.")
    logger.debug(f"my_task function reference: {my_task}")
    my_task.delay()
    logger.info("my_task dispatched asynchronously via Celery.")
    return HttpResponse("Hello, world! This is the home page.")

def test_view(request):
    logger.info("test_view accessed.")
    return HttpResponse('This is a test view. It should not be cached.')