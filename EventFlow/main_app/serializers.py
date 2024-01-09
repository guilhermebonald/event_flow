from rest_framework import serializers
from .models import UserModel, EventModel


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = UserModel
        fields = "__all__"

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            # Adicione aqui outros campos conforme necessário
        )
        return user


class EventSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = EventModel
        fields = "__all__"
