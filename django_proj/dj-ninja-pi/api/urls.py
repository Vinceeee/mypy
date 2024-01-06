from django.urls import path
from ninja import NinjaAPI
from .views import router

api = NinjaAPI()


api.add_router("/cal/",router, tags=["cal"])


urlpatterns = [path("", api.urls)]
