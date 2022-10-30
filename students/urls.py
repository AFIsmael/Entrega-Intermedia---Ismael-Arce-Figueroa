from django.urls import path

from students import views

app_name = "student"
urlpatterns = [
    path("students", views.students, name="student-list"),
]