from django.contrib import admin

# Register your models here.
from accounts.models import Account, TeacherProfile

admin.site.register(Account)
admin.site.register(TeacherProfile)
