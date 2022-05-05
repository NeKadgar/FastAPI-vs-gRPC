# Cool! https://github.com/rnevius/minimal-django
import sys
import time

from django.conf import settings
from django.urls import path
from django.core.management import execute_from_command_line
from django.http import HttpResponse, JsonResponse
from django.db import models
import logging

logging.disable(logging.INFO)

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=sys.modules[__name__],
)
count = 0
start_time = time.time()


def index(request):
    return HttpResponse('<h1>A minimal Django response!</h1>')


def hello_name(request, name):
    global count, start_time
    count += 1
    if count % 1000 == 0:
        print(f"1000 Hellow in {time.time() - start_time}")
        start_time = time.time()
    return JsonResponse({"message": f"Hello {name}!"})


urlpatterns = [
    path(r'', index),
    path('hello/<str:name>', hello_name),
]


if __name__ == '__main__':
    execute_from_command_line(sys.argv)
