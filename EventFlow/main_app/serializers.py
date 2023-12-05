from rest_framework import serializers
from .models import CustomUser

# from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser
        fields = "__all__"
        # or fields = ["name"]
