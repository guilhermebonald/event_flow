from django.contrib import admin
from django.urls import path, include
from main_app.views import UserRegisterView, EventCreatorView, UserGetDataView


urlpatterns = [
    path("register/", UserRegisterView.as_view()),
    path("home/<username>/", UserGetDataView.as_view()),
    path("new_event/", EventCreatorView.as_view()),
    path("event/<int:event_id>/", EventCreatorView.as_view()),
]
