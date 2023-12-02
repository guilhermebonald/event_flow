from rest_framework import serializers
from django.contrib.auth.models import User

# from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = "__all__"
        # or fields = ["name"]
