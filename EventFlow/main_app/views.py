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


# ANCHOR INCREMENTAR TRATAMENTO DE ERROS.
# FIXME ADICIONAR AUTH.
class CreateEvent(APIView):
    def post(self, request):
        user = get_object_or_404(UserModel, username=request.data["usuario"])
        request.data["usuario"] = user.id
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# FIXME PRECISA RETORNAR O EVENTO PELO ID OU SE NÃO RETORNAR TODOS OS EVENTOS. TRATA ERROS AQUI.
class GetEvent(APIView):
    def get(self, request, event_id=None):
        if event_id:
            try:
                event = EventModel.objects.get(id=event_id)
                serializer = EventSerializer(event, data=request.data)
                if serializer.is_valid():
                    return Response(serializer.data)
                else:
                    return Response(
                        {"Error": "Dados inválidos", "Details": serializer.errors},
                        status=400,
                    )

            except EventModel.DoesNotExist:
                return Response({"Error": "Evento não encontrado"}, status=404)
        else:
            events = EventModel.objects.all()
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data)


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
                serializer = EventSerializer(event, data=request.data)
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


# FIXME PRECISA SER ADICIONADO A CAMADA DE AUTENTICAÇÃO.
# FIXME FAZER A VALIDAÇÃO ENTRE USUARIO LOGADO E USUARIO CRIADOR DO EVENTO
class DeleteEvent(APIView):
    def delete(self, request, event_id=None):
        if event_id:
            event = get_object_or_404(EventModel, id=event_id)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        else:
            events = EventModel.objects.all()
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data)
