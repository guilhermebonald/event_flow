from django.contrib import admin
from django.urls import path, include
from main_app import views


urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
]
