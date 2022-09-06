from django.urls import path
from .views import AssignTeacherView, ClassRetrieveUpdateDeleteView,ClassView

app_name = 'classes'

urlpatterns = [
    path('class-view/', ClassView.as_view(), name='class_view'),
    path('assign-teachers/<int:pk>/', AssignTeacherView.as_view()),
    path('class-view/<int:class_id>/', ClassRetrieveUpdateDeleteView.as_view()),
]
