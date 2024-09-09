from django.urls import path
from .views import course_list, add_course

urlpatterns = [
    path('courses', course_list, name='course_list'),  # URL for course list
    path('create_course', add_course, name='add_course'),  # Your course creation URL
]
