from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from main_app.serializers import UserSerializer, EventSerializer
from .models import UserRegister, Event
from django.shortcuts import get_object_or_404
from rest_framework import status


# Register User
class UserRegisterView(APIView):
    def get(self, request, username=None):
        self.authentication_classes = [SessionAuthentication, BasicAuthentication]
        self.permission_classes = [IsAuthenticated]

        if username:
            user = get_object_or_404(UserRegister, username=username)
            serializer = UserSerializer(user)
        else:
            users = UserRegister.objects.all()
            serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# Create Event
class EventCreatorView(APIView):
    def get(self, request, event_id=None):
        if event_id:
            event = get_object_or_404(Event, id=event_id)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        else:
            events = Event.objects.all()
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data)

    def post(self, request):
        user = get_object_or_404(UserRegister, username=request.data["usuario"])
        request.data["usuario"] = user.id
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
