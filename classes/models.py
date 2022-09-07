from django.db import models
from slugify import slugify

# Create your models here.
from accounts.models import TeacherProfile


class ClassGrade(models.Model):
    teacher = models.ManyToManyField(TeacherProfile)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='class_grades')

    def __str__(self):
        return self.name


class Questions(models.Model):
    category = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    difficulty = models.CharField(max_length=10)
    question_text = models.TextField()
    slug_text = models.CharField(max_length=100, null=True)

    def save(self, *args, **kwargs):
        self.slug_text = slugify(self.question_text, max_length=15, word_boundary=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category
