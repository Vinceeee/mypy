from django.urls import path
from ninja import NinjaAPI
from .views import router
from .ws import MyWS

api = NinjaAPI()
api.add_router("/cal/", router, tags=["cal"])
urlpatterns = [path("", api.urls)]
ws_patterns = [path("ws", MyWS.as_asgi())]
