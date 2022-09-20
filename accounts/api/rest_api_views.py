from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.models import TeacherProfile
from accounts.api.serializers import TeacherProfileListSerializer, TeacherProfileRetrieveUpdateDestroySerializer, \
    UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer_class = UserSerializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        return Response(serializer_class.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        try:
            user = get_user_model().objects.get(email=email)
        except:
            raise AuthenticationFailed('Email does not exist')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password!')

        return Response(
            {
                'message': 'success'
            }
        )


class TeacherListAPIView(ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
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
