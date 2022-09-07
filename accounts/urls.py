from django.urls import path

from .views import AddFakeData, TeacherRetrieveUpdateDeleteView, TeacherView

app_name = 'accounts'

urlpatterns = [
    path('teacher-view/', TeacherView.as_view(), name='teacher_view'),
    path('teachers/<int:teacher_id>/', TeacherRetrieveUpdateDeleteView.as_view()),
    path('add-fake-teacher/', AddFakeData.as_view()),
]
