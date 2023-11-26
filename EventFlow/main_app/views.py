from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import User
from django.http import HttpResponse, JsonResponse


@api_view(["GET"])
def user_manager(request):
    if request.method == "GET":
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)
