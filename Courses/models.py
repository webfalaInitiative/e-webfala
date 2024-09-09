from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Course(models.Model):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)  # Use Django’s built-in user model
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price with up to 6 digits and 2 decimal places
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
