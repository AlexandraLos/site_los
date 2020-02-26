from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Определенные ранее обработчики.
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]