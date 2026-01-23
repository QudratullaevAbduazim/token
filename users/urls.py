from . import views
from django.urls import path
from django.urls import path

urlpatterns = [
    path("login/", views.LoginView.as_view()),
    path("register/", views.RegisterView.as_view()),
    path("users/", views.UserListAPIView.as_view()),
    path("create-user/", views.CreateUserAPIView.as_view()),
    path("update-user/<int:pk>/", views.UpdateUserAPIView.as_view()),
    path("user-detail/<int:pk>/", views.DetailUserAPIView.as_view()),
    path("delete-user/<int:pk>/", views.DeleteUserAPIView.as_view()),
    
]
    