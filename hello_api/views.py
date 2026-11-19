import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from .entities.user import User
from .entities.animal import Animal
from .entities.comic import Comic
from .entities.result import ResultDto



def index(request):
    return JsonResponse({
        "message": "Hello world"
    })

@csrf_exempt
@require_POST
def save_comic(request):
    data = json.loads(request.body)

    comic = Comic(
        title=data["title"],
        description=data["description"],
        editorial=data["editorial"],
    )
    comic.save()

    return JsonResponse({
        "id": comic.id,
        "title": comic.title,
        "description": comic.description,
        "editorial": comic.editorial
    }, status=201)


@require_http_methods(["GET"])
def get_all_comics(request):
    comics = list(Comic.objects.values("id", "title", "description", "editorial"))
    return JsonResponse(comics, safe=False)


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def comic_by_id(request, id):
    # Busca el cómic; si no existe, responde 404
    try:
        comic = Comic.objects.get(id=id)
    except Comic.DoesNotExist:
        return JsonResponse({"message": f"No existe un comic con id {id}"}, status=404)

    # GET: obtener uno
    if request.method == "GET":
        return JsonResponse({
            "id": comic.id,
            "title": comic.title,
            "description": comic.description,
            "editorial": comic.editorial
        })

    # PUT: actualizar
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"message": "El JSON enviado no es valido"}, status=400)

        comic.title = data.get("title", comic.title)
        comic.description = data.get("description", comic.description)
        comic.editorial = data.get("editorial", comic.editorial)
        comic.save()

        return JsonResponse({
            "id": comic.id,
            "title": comic.title,
            "description": comic.description,
            "editorial": comic.editorial
        })

    # DELETE: eliminar
    comic.delete()
    return JsonResponse({"message": f"Comic {id} eliminado correctamente"})