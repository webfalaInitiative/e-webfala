from django.shortcuts import render, get_object_or_404
from Courses.models import Course


# Create your views here.
def payments(request):
    course_id = request.GET.get("course_id")
    course = get_object_or_404(Course, id=course_id)

    context = {"course": course}
    return render(request, "payments.html", context)
