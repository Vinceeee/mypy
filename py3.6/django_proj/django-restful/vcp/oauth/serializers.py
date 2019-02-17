from rest_framework import serializers as slzers
from oauth.models import User


class UserSerializer(slzers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'user_name')
