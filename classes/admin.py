from django.contrib import admin

# Register your models here.
from classes.models import ClassGrade, Questions

admin.site.register(ClassGrade)
admin.site.register(Questions)
