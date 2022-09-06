from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import TeacherView, TeacherRetrieveUpdateDeleteView

app_name = 'accounts'

urlpatterns = [
    path('teacher-view/', TeacherView.as_view(), name='teacher_view'),
    path('teachers/<int:teacher_id>/', TeacherRetrieveUpdateDeleteView.as_view()),
]
