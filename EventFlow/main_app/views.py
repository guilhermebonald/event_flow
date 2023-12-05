from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from main_app.serializers import UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user": serializer.data})
