from django.urls import path
from event_app.views import (
    CreateEvent,
    GetEvent,
    UpdateEvent,
    DeleteEvent,
)
from main_app.views import (
    RegisterUser,
    GetUser,
    UpdateUser,
    DeleteUser,
)


urlpatterns = [
    path("users/register/", RegisterUser.as_view()),
    path("users/home/<username>/", GetUser.as_view()),
    path("users/delete/<username>/", DeleteUser.as_view()),
    path("users/change-user/<username>/", UpdateUser.as_view()),
    path("users/events/<username>/create/", CreateEvent.as_view()),
    path("users/events/<int:event_id>/", GetEvent.as_view()),
    path("users/events/update/<int:event_id>/", UpdateEvent.as_view()),
    path("users/events/delete/<int:event_id>/", DeleteEvent.as_view()),
]
