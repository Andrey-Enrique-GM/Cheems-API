import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from .entities.comic import Comic
from .entities.result import ResultDto
from django.db import DatabaseError

def comic_to_dict(comic):
    return {
        "id": comic.id,
        "title": comic.title,
        "description": comic.description,
        "editorial": comic.editorial,
    }

def index(request):
    return JsonResponse({
        "message": "Hello world"
    })

@csrf_exempt
@require_POST
def save_comic(request):
    # 400: JSON inválido, se truena quitando los {}
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"message": "El JSON enviado no es valido, favor de enviarlo como formato JSON"}, status=400)

    # 400: el JSON debe ser un objeto, truena si ponemos [] afuera del {}
    if not isinstance(data, dict):
        return JsonResponse({"message": "El cuerpo debe ser un objeto JSON"}, status=400)

    # 400: faltan campos obligatorios, truena si el nombre de los atributos no son correcto o si estan mal escrotos
    required = ["title", "description", "editorial"]
    missing = [f for f in required if f not in data]
    if missing:
        return JsonResponse(
            {"message": f"Faltan campos obligatorios favor de completar o escribir bien el nombre de los atributos solo tenemos 3 atributos que ocupa escribir bien (title,description,editorial): {', '.join(missing)}"},
            status=400,
        )

    # 422: campos con valores inválidos (vacíos o no son texto), truena si estan vacios o si quitas las comillas
    invalid = [f for f in required if not isinstance(data[f], str) or not data[f].strip()]
    if invalid:
        return JsonResponse(
            {"message": f"Los siguientes campos no son validos estan vacios o no son texto: {', '.join(invalid)}"},
            status=422,
        )

    # 500: error al guardar en la base de datos, muy complicado de tronar, pero puede pasar si la base de datos no esta disponible o si hay un error en la base de datos
    try:
        comic = Comic.objects.create(
            title=data["title"].strip(),
            description=data["description"].strip(),
            editorial=data["editorial"].strip(),
        )
    except DatabaseError:
        return JsonResponse({"message": "Error al guardar el comic"}, status=500)

    # 201: creado
    return JsonResponse(comic_to_dict(comic), status=201)

######################################################################

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