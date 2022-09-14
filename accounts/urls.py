from django.urls import path

from accounts.views.simple_views import AddFakeData, TeacherRetrieveUpdateDeleteView, TeacherView
from accounts.views.model_views import TeacherDetailView, TeacherListView, TeacherDeleteView, TeacherUpdateView, \
    TeacherCreateView

app_name = 'accounts'

urlpatterns = [
    # Simple Views
    path('teacher-view/', TeacherView.as_view(), name='teacher_view'),
    path('teachers/<int:teacher_id>/', TeacherRetrieveUpdateDeleteView.as_view()),
    path('add-fake-teacher/', AddFakeData.as_view()),

    # Model Views
    path('teacher-list/', TeacherListView.as_view(), name="Teacher_List"),
    path('teacher-create/', TeacherCreateView.as_view(), name="Teacher_Create"),
    path('teacher-detail/<uuid:id>/', TeacherDetailView.as_view(), name="Teacher_Detail"),
    path('teacher-delete/<uuid:id>/', TeacherDeleteView.as_view(), name="Teacher_Delete"),
    path('teacher-update/<uuid:id>/', TeacherUpdateView.as_view(), name="Teacher_Update")
]
