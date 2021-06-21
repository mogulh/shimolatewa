from django.urls import path
from . import views


urlpatterns = [
    path("", views.school, name="school"),
    path("staff", views.staff, name="staff"),
    path("students", views.students, name="students"),
    path("classes", views.classes, name="classes"),
    path("clubs", views.clubs, name="clubs"),
    path("games", views.games, name="games"),
]
