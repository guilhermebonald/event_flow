from django.urls import path, include
from main_app.views import (
    RegisterUser,
    UpdateUser,
    CreateEvent,
    GetEvent,
    GetUser,
    DeleteUser,
)


urlpatterns = [
    path("users/register/", RegisterUser.as_view()),
    path("users/home/<username>/", GetUser.as_view()),
    path("users/delete/<username>/", DeleteUser.as_view()),
    path("users/change-user/<username>/", UpdateUser.as_view()),
    path("users/create-event/", CreateEvent.as_view()),
    path("users/events/<int:event_id>/", GetEvent.as_view()),
]
