from django.contrib.auth.models import User, Group
import rest_framework
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class SentimenPartaiSerializer(serializers.Serializer):
    query = serializers.CharField()
    tweets = serializers.ListField(
        child=serializers.CharField(),
    )