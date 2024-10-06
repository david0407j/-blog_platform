from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Página inicial (lista de posts)
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Página de detalhes do post
]

