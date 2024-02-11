from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from main_app.serializers import UserSerializer
from .models import UserModel
from rest_framework import status


# * Regras de Usuarios
class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(
                {"Error": "Dados inválidos", "Details": serializer.errors},
                status=400,
            )


class GetUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, username=None):
        user = request.user
        if str(user.username) == username:
            try:
                user = UserModel.objects.get(username=username)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            except UserModel.DoesNotExist:
                return Response({"Error": "Usuário não encontrado"}, status=404)
        else:
            return Response({"detail": "Acesso negado"}, status=403)


class UpdateUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, username=None):

        try:
            user = UserModel.objects.get(username=username)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response(
                    {"Error": "Dados inválidos", "Details": serializer.errors},
                    status=400,
                )
        except UserModel.DoesNotExist:
            return Response({"Error": "Usuário não encontrado"}, status=404)


class DeleteUser(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, username=None):
        if username == request.user.username:
            try:
                user = UserModel.objects.get(username=username)
                user.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except UserModel.DoesNotExist:
                return Response({"Error": "Usuário não encontrado"}, status=404)
        else:
            return Response({"detail": "Acesso negado"}, status=403)
