from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:  # Corrected capitalization
        model = Course
        fields = ['title', 'description', 'price']
