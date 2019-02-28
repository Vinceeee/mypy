from rest_framework import generics

from lottery.models import Candidate, Price, Winner
from lottery.serializers import CandidateSerializer, PriceSerializer, WinnerSerializer


class CandidateApi(generics.ListCreateAPIView):
    """
    list / create candidate
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class PriceApi(generics.ListCreateAPIView):
    """
    list / create Price
    """
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class WinnerApi(generics.ListCreateAPIView):
    """
    list / create winner
    """
    queryset = Winner.objects.all()
    serializer_class = WinnerSerializer
