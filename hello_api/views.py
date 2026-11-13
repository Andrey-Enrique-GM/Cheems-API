import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .entities.user import User
from .entities.animal import Animal
from .entities.result import ResultDto



def index(request):
    return JsonResponse({
        "message": "Hello world"
    })


@csrf_exempt
@require_POST
def save_user(request):
    try:
        data = json.loads(request.body)

        name = data["name"]
        account = data["account"]

        # Validación para evitar campos vacíos ("") o con solo espacios ("   ")
        if not str(name).strip() or not str(account).strip():
            result = ResultDto(0, False, "El nombre y la cuenta no pueden estar vacíos.")
            return JsonResponse(result.to_dict(), status=400)

        user = User(data["id"], name, account)

        result = ResultDto(user.id, True, f"Usuario '{user.name}' registrado correctamente.")
        return JsonResponse(result.to_dict(), status=201)

    except KeyError as e:
        result = ResultDto(0, False, f"Falta el campo obligatorio en el JSON: {str(e)}")
        return JsonResponse(result.to_dict(), status=400)
    except json.JSONDecodeError:
        result = ResultDto(0, False, "El formato del JSON enviado no es valido.")
        return JsonResponse(result.to_dict(), status=400)
    except Exception as e:
        result = ResultDto(0, False, f"Error inesperado al guardar: {str(e)}")
        return JsonResponse(result.to_dict(), status=500)


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
