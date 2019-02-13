from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .apps import logger


def home(req):
    logger.info("access home")
    response = {"message": "cao"}
    return JsonResponse(response)


def login(req, account, passwd):
    """TODO: Docstring for login.
    :account: login_account
    :passwd: login_passwd
    :returns: redirect to logined page or logout
    """
    logger.info("login {}".format(account))
    return HttpResponseRedirect("/nima")
