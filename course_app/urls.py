from . import views
from django.urls import path

app_name = "course_app"
urlpatterns = [
    path("course_list", views.course_list, name="course_list"),
    path("course_buying/<int:pk>", views.course_buy, name="course_buying"),
    path("user_courses", views.user_courses, name="user_courses"),
    path("course_detail/<int:pk>", views.course_detail, name="course_detail"),
]
