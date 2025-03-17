from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.RegisterUser, name='register_user'),
    path('login/', views.LoginUser, name='login_user'),
]