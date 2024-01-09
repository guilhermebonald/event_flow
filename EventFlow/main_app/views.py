from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from main_app.serializers import UserSerializer, EventSerializer
from .models import UserModel, EventModel
from django.shortcuts import get_object_or_404
from rest_framework import status


# * Regras de Usuarios
class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class GetUser(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, username=None):
        if username == request.user.username:
            user = get_object_or_404(UserModel, username=username)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({"Error": "Nenhum Usuário Encontrado"}, status=403)


# ! Testar e fazer alterações
class UpdateUser(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, username=None):
        user = get_object_or_404(UserModel, username=username)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# ! Alterar o ID pelo nome de usuario.
class DeleteUser(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk=None):
        if int(pk) == request.user.id:
            primary_key = get_object_or_404(UserModel, id=pk)
            primary_key.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "Nenhum Usuario Encontrado"}, status=403)


# * Regras de Eventos
class CreateEvent(APIView):
    def post(self, request):
        user = get_object_or_404(UserModel, username=request.data["usuario"])
        request.data["usuario"] = user.id
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetEvent(APIView):
    def get(self, request, event_id=None):
        if event_id:
            event = get_object_or_404(EventModel, id=event_id)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        else:
            events = EventModel.objects.all()
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data)
