from django.shortcuts import render


# Create your views here.
def student(request):
    return render(request, 'student.html')


def instructor(request):
    return render(request, 'instructor.html')