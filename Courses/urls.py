from django.urls import path
from .views import course_list, course_create_title, course_create_category, course_create_price, course_review,instructor_dashboard,upload_lesson,course_detail

urlpatterns = [
    path('instructor_dashboard', instructor_dashboard, name='instructor_dashboard'),
    path('add_title', course_create_title, name='course_create_title'),
    path('add_category', course_create_category, name='course_create_category'),
    path('add_price', course_create_price, name='course_create_price'),
    path('add_lessons', upload_lesson, name='course_create_lessons'),
    path('review_course', course_review, name='course_review'),
    path('', course_list, name='course_list'),  # URL for course list
    path('course/<int:course_id>/', course_detail, name='course_detail'),
]
