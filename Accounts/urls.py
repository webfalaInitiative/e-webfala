from django.urls import path
<<<<<<< HEAD

urlpatterns = [
    
]
=======
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('student/', views.student, name='student'),
    path('instructor/', views.instructor, name='instructor'),
]
>>>>>>> payments
