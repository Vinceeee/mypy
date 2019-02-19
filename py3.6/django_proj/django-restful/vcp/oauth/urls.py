from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user', views.user),
    path('login', views.login),
    path('upload', views.upload_file),
]
