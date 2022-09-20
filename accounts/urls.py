from django.urls import path

from accounts.api.rest_api_views import TeacherListAPIView, TeacherRetrieveUpdateDestroyAPIView, \
    TeacherListCreateAPIView, RegisterView, LoginView
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
    path('teacher-update/<uuid:id>/', TeacherUpdateView.as_view(), name="Teacher_Update"),

    # REST API Views

    path('v1/register/', RegisterView.as_view(), name="register_account"),
    path('v1/login/', LoginView.as_view(), name="login_account"),

    path('v1/teacher-list/', TeacherListAPIView.as_view(), name="teacher_list_api"),
    path('v1/teacher-list-create/', TeacherListCreateAPIView.as_view(), name="teacher_list_create_api"),
    path('v1/teacher-crud/<uuid:id>/', TeacherRetrieveUpdateDestroyAPIView.as_view(), name="teacher_crud_api"),
]
