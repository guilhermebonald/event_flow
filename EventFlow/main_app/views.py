from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from main_app.serializers import (
    UserSerializer,
    EventSerializer,
    EventUpdateSerializer,
    GetEventSerializer,
)
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
        else:
            return Response(
                {"Error": "Dados inválidos", "Details": serializer.errors},
                status=400,
            )


class GetUser(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, username=None):
        if username == request.user.username:
            try:
                user = UserModel.objects.get(username=username)
                serializer = UserSerializer(user, data=request.data)
                if serializer.is_valid():
                    return Response(serializer.data)
                else:
                    return Response(
                        {"Error": "Dados inválidos", "Details": serializer.errors},
                        status=400,
                    )
            except UserModel.DoesNotExist:
                return Response({"Error": "Usuário não encontrado"}, status=404)
        else:
            return Response({"Error": "Acesso negado"}, status=403)


class UpdateUser(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, username=None):
        if username == request.user.username:
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
        else:
            return Response({"Error": "Acesso negado"}, status=403)


class DeleteUser(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
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


# * Regras de Eventos


# ANCHOR TENTAR TIRAR A NECESSIDADE DE TER QUE PASSAR "USER_ID" NO BODY DA REQUISIÇÃO
class CreateEvent(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, username):
        if request.user.username == username:
            try:
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                return Response({"Error": "Usuario não encontrado"}, status=404)

            request.data["user_id"] = user
            serializer = EventSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Acesso negado"}, status=403)


class GetEvent(APIView):
    def get(self, request, event_id=None):
        try:
            event = EventModel.objects.get(id=event_id)
            serializer = GetEventSerializer(event, data=request.data)
            if serializer.is_valid():
                return Response(serializer.data)
            else:
                return Response(
                    {"Error": "Dados inválidos", "Details": serializer.errors},
                    status=400,
                )

        except EventModel.DoesNotExist:
            return Response({"Error": "Evento não encontrado"}, status=404)


# FIXME CRIAR VIEW
class GetAllEvent(APIView):
    pass


class UpdateEvent(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, event_id=None):
        try:
            user = UserModel.objects.get(id=request.data["user_id"])
        except UserModel.DoesNotExist:
            return Response({"Error": "Usuário não encontrado"}, status=404)

        if str(user) == request.user.username:
            try:
                event = EventModel.objects.get(id=event_id)
                serializer = EventUpdateSerializer(event, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=201)
                else:
                    return Response(
                        {"Error": "Dados inválidos", "Details": serializer.errors},
                        status=400,
                    )
            except EventModel.DoesNotExist:
                return Response({"Error": "Evento não encontrado"}, status=404)
        else:
            return Response({"detail": "Acesso negado"}, status=403)


class DeleteEvent(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, event_id=None):
        event = EventModel.objects.get(id=event_id)
        user_id = event.user_id
        if str(user_id) == request.user.username:
            try:
                event = EventModel.objects.get(id=event_id)
                event.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except EventModel.DoesNotExist:
                return Response({"Error": "Evento não encontrado"}, status=404)
        else:
            return Response({"detail": "Acesso negado"}, status=403)
