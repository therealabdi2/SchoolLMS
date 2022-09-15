from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView

from accounts.models import TeacherProfile
from accounts.api.serializers import TeacherProfileListSerializer, TeacherProfileRetrieveUpdateDestroySerializer


class TeacherListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TeacherProfileListSerializer

    def get_queryset(self):
        return TeacherProfile.objects.all()


class TeacherListCreateAPIView(ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = TeacherProfileListSerializer

    def get_queryset(self):
        return TeacherProfile.objects.all()


class TeacherRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileRetrieveUpdateDestroySerializer
