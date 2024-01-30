from rest_framework import serializers
from event_app.models import EventModel


class EventSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = EventModel
        fields = "__all__"


class GetEventSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = EventModel
        fields = "__all__"
        # To set "required=False" in all model instances.
        extra_kwargs = {
            field.name: {"required": False} for field in EventModel._meta.get_fields()
        }


class EventUpdateSerializer(serializers.ModelSerializer):
    """
    O serializer "user_id" foi deixado como obrigatorio, para a validação na view "UpdateEvent",
    pois é necessario validar se o usuario criador do evento é o mesmo que está sendo logado.
    """

    nome = serializers.CharField(required=False)
    data = serializers.DateField(required=False)
    tipo = serializers.CharField(required=False)
    presenca = serializers.CharField(required=False)
    comentarios = serializers.CharField(required=False)

    class Meta(object):
        model = EventModel
        fields = "__all__"

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
