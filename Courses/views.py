from django.shortcuts import render,redirect
from .models import Course
from .form import CourseForm 

# Create your views here.



def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            return redirect('course_list')  # Redirect to the course list view
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})



def course_list(request):
    courses = Course.objects.all()  # Retrieve all courses from the database
    return render(request, 'course_list.html', {'courses': courses})

