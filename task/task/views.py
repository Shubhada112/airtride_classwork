import json
import os

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

USER_FILE = os.path.join(settings.BASE_DIR, "user.json")
TASK_FILE = os.path.join(settings.BASE_DIR, "task.json")


def _read_json_file(file_path):
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def _write_json_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


@csrf_exempt
def add_user(request):
    if request.method == "GET":
        users = _read_json_file(USER_FILE)
        return JsonResponse(users, safe=False, status=200)
    if request.method != "POST":
        return JsonResponse({"error": "Only GET and POST allowed"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)
    users = _read_json_file(USER_FILE)

    new_user = {
        "id": data["id"],
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "age": data["age"],
    }

    users.append(new_user)
    _write_json_file(USER_FILE, users)

    return JsonResponse(new_user, status=201)


def get_users(request):
    if request.method != "GET":
        return JsonResponse({"error": "Only GET allowed"}, status=405)

    users = _read_json_file(USER_FILE)
    return JsonResponse(users, safe=False, status=200)


@csrf_exempt
def add_task(request):
    if request.method == "GET":
        tasks = _read_json_file(TASK_FILE)
        return JsonResponse(tasks, safe=False, status=200)
    if request.method != "POST":
        return JsonResponse({"error": "Only GET and POST allowed"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)
    tasks = _read_json_file(TASK_FILE)

    new_task = {
        "id": data["id"],
        "user_id": data["user_id"],
        "name": data["name"],
        "desc": data["desc"],
    }

    tasks.append(new_task)
    _write_json_file(TASK_FILE, tasks)

    return JsonResponse(new_task, status=201)


def get_tasks(request):
    if request.method != "GET":
        return JsonResponse({"error": "Only GET allowed"}, status=405)

    tasks = _read_json_file(TASK_FILE)
    return JsonResponse(tasks, safe=False, status=200)
