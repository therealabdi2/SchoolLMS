import uuid

from django.db import models
from slugify import slugify

# Create your models here.
from accounts.models import TeacherProfile


class ClassGrade(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, null=False, editable=False, default=uuid.uuid4
    )
    teacher = models.ManyToManyField(TeacherProfile)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='class_grades')

    def __str__(self):
        return self.name


class Questions(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, null=False, editable=False, default=uuid.uuid4
    )
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
