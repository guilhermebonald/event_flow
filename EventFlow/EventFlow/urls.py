from django.contrib import admin
from django.urls import path
from main_app import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "login/",
        views.login,
    ),
    path("signup/", views.signup),
    path("auth_token/", views.test_token),
]
