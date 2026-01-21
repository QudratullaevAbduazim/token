from . import views
from django.urls import path
from django.urls import path

urlpatterns = [
    path("login/", views.LoginView.as_view()),
    path("register/", views.RegisterView.as_view()),
    path("users/", views.UserListAPIView.as_view()),
]
    