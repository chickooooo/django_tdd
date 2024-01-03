from django.contrib import admin
from django.urls import path
from core import views


# url paths
urlpatterns = [
    # admin dashboard
    path("admin/", admin.site.urls, name="admin dashboard"),
    # health check
    path("api/health/", views.Health.as_view(), name="health check"),
]
