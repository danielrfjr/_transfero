from django.urls import path
from usuarios import views

urlpatterns = [
    path('cadastro/', views.criarUsuario, name='criarUsuario'),
    path('login/', views.login, name='login'),
]











