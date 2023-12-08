from rest_framework.response import Response
from rest_framework.views import APIView
from main_app.serializers import UserSerializer
from .models import CustomUser


class RegisterView(APIView):
    def get(self, request):
        user = CustomUser.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
