import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .entities.user import User
from .entities.animal import Animal



def index(request):
    return JsonResponse({
        "message": "Hello world"
    })


@csrf_exempt
@require_POST
def save_user(request):
    data = json.loads(request.body)

    user = User(data["id"], data["name"], data["account"])

    return JsonResponse({
        "id": user.id,
        "name": user.name,
        "account": user.account
    }, status=201)


@csrf_exempt
@require_POST
def save_animal(request):
    data = json.loads(request.body)

    animal = Animal(data["id"], data["name"], data["color"])

    return JsonResponse({
        "id": animal.id,
        "name": animal.name,
        "color": animal.color
    }, status=201)
