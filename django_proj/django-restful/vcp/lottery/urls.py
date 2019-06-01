from django.urls import path

from . import views

urlpatterns = [
    path('candidate', views.CandidateApi.as_view()),
    path('candidate/<int:pk>', views.CandidateApi.as_view()),
    path('prices', views.PriceApi.as_view()),
    path('prices/<int:pk>', views.PriceApi.as_view()),
    path('winner', views.WinnerApi.as_view()),
    path('winner/<int:pk>', views.WinnerApi.as_view()),
]
