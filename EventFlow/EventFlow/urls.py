from django.urls import path
from event_app.views import (
    CreateEvent,
    GetEvent,
    GetAllEvent,
    UpdateEvent,
    DeleteEvent,
)
from main_app.views import (
    RegisterUser,
    GetUser,
    UpdateUser,
    DeleteUser,
)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # JWT
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # URLS
    path("users/register/", RegisterUser.as_view()),
    path("users/home/<username>/", GetUser.as_view()),
    path("users/delete/<username>/", DeleteUser.as_view()),
    path("users/change-user/<username>/", UpdateUser.as_view()),
    path("users/events/<username>/create/", CreateEvent.as_view()),
    path("users/events/<int:event_id>/", GetEvent.as_view()),
    path("users/events/", GetAllEvent.as_view()),
    path("users/events/update/<int:event_id>/", UpdateEvent.as_view()),
    path("users/events/delete/<int:event_id>/", DeleteEvent.as_view()),
]
