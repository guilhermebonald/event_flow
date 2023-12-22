from rest_framework import serializers
from .models import UserRegister, Event


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = UserRegister
        fields = "__all__"

    def create(self, validated_data):
        user = UserRegister.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            # Adicione aqui outros campos conforme necessário
        )
        return user


class EventSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Event
        fields = "__all__"
