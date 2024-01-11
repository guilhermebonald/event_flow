from rest_framework import serializers
from .models import UserModel, EventModel


class UserSerializer(serializers.ModelSerializer):
    # Necessario ter os campos username e password com "required=False" para que no metodo update não tenha que inserir senha e login no body.
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False, write_only=True)

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

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class EventSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = EventModel
        fields = "__all__"
