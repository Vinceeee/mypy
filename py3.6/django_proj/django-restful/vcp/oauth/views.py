import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from oauth.models import User
from oauth.serializers import UserSerializer


# def index(req: HttpRequest) -> HttpResponse:
def index(req) -> HttpResponse:
    return HttpResponse("Hi")


@csrf_exempt
def user(req):
    """
    user's actions
    """
    if req.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif req.method == 'POST':
        body = json.loads(req.body)
        user = User()
        user.user_name = body['name']
        user.user_passwd = body['passwd']
        user.save()
        return JsonResponse({"msg": "created"}, status=201)
    else:
        return JsonResponse(serializer.errors, status=405)


@csrf_exempt
def login(req):
    """
    login
    """
    if req.method != "POST":
        return JsonResponse({}, status=405)

    body = json.loads(req.body)
    user_name = body.get('name', "")
    user_passwd = User.hashing(user_name, body.get("passwd", ""))
    if User.objects.get(user_name=user_name, user_passwd=user_passwd):
        return JsonResponse({"token": user_passwd}, status=200)
    return JsonResponse({}, status=404)
