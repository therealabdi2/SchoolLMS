from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import TeacherView, TeacherUpdateDeleteView

app_name = 'accounts'

urlpatterns = [
    path('teacher-view/', TeacherView.as_view(), name='teacher_view'),
    path('teachers/<int:teacher_id>/', TeacherUpdateDeleteView.as_view(), name='teacher_edit'),
]
