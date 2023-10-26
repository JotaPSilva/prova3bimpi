from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("novo_disco", views.create_disco, name="create_disco"),
    path("editar_disco/<int:pk>", views.edit_disco, name="edit_disco"),
    path("excluir_disco/<int:pk>", views.delete_disco, name="delete_disco"),
    path("accounts/login",LoginView.as_view(template_name="disco/accounts/login.html"),name="login"),
    path("accounts/logout",LogoutView.as_view(),name="logout"),
]
