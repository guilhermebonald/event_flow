from rest_framework import serializers
from .models import Users, Events


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Users
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Events
        fields = "__all__"
