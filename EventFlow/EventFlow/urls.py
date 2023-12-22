from django.contrib import admin
from django.urls import path, include
from main_app.views import UserRegisterView, EventCreatorView


urlpatterns = [
    path("register/<username>/", UserRegisterView.as_view()),
    path("new_event/", EventCreatorView.as_view()),
    path("event/<int:event_id>/", EventCreatorView.as_view()),
]
