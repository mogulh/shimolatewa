from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("/news", views.news, name="news"),
    path("/n/<str:slug>", views.news_detail, name="n_detail"),
    path("/gallery", views.gallery, name="gallery"),
    path("/articles", views.articles, name="articles"),
    path("/a/<str:slug>", views.article_detail, name="a_detail"),
]
