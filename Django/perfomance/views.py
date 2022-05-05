import time
import json

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from perfomance.models import User

count = 0
start_time = time.time()


def hello_name(request, name):
    global count, start_time
    count += 1
    if count % 1000 == 0:
        print(f"1000 Hellow in {time.time() - start_time}")
        start_time = time.time()
    return JsonResponse({"message": f"Hello {name}!"})


@csrf_exempt
def add_user(request):
    global count, start_time
    data = json.loads(request.body)
    new_user = User.objects.create(**data)
    count += 1
    if count % 100 == 0:
        print(f"100 users in {time.time() - start_time}")
        start_time = time.time()
    return JsonResponse({"user_id": new_user.id})


@csrf_exempt
def auth_user(request):
    global count, start_time
    data = json.loads(request.body)
    user = User.objects.filter(**data).first()
    count += 1
    if count % 1000 == 0:
        print(f"1000 auth in {time.time() - start_time}")
        start_time = time.time()
    return JsonResponse({"token": f'{user.first_name}_{user.last_name}'})
