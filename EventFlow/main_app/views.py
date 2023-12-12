from rest_framework.response import Response
from rest_framework.views import APIView
from main_app.serializers import UserSerializer, EventSerializer
from .models import Users, Events


# Register User
class UserRegisterView(APIView):
    def get(self, request):
        user = Users.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# Create Event
class EventCreatorView(APIView):
    def get(self, request):
        events = Events.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = Users.objects.get(id=request.data["id"])
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(usuario=user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
