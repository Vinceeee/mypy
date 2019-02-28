from rest_framework import serializers as slzers
from lottery.models import Candidate, Price, Winner


class CandidateSerializer(slzers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('c_id', 'c_name', 'c_description')


class PriceSerializer(slzers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('p_id', 'p_name', 'p_level', 'p_pic', 'p_istaken')


class WinnerSerializer(slzers.ModelSerializer):
    class Meta:
        model = Winner
        fields = ('w_id', 'candidate', 'price', 'policy')
