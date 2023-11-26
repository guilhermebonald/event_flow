from django.contrib import admin
from django.urls import path
from main_app import views


# router = routers.DefaultRouter()
# router.register(r"users", views.user_manager)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "user",
        views.user_manager,
    ),
]
