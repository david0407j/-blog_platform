from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),  # URL da lista de posts
    path(
        "post/<slug:slug>/", views.post_detail, name="post_detail"
    ),  # URL para detalhes do post
]
