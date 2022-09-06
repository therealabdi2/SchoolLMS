from django.db import models

# Create your models here.
from accounts.models import TeacherProfile


class ClassGrade(models.Model):
    teacher = models.ManyToManyField(TeacherProfile)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='class_grades')

    def __str__(self):
        return self.name
