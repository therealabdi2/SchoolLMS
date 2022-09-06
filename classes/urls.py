from django.urls import path
from .views import ClassView, AssignTeacherView

app_name = 'classes'

urlpatterns = [
    path('class-view/', ClassView.as_view(), name='class_view'),
    path('assign-teachers/<int:pk>/', AssignTeacherView.as_view())
    # path('class/<int:class_id>/', CLassRetrieveUpdateDeleteView.as_view()),
]
