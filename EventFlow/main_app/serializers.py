from rest_framework import serializers
from .models import UserRegister, Event


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = UserRegister
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Event
        fields = "__all__"
