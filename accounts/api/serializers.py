from rest_framework import serializers

from accounts.models import TeacherProfile


class TeacherProfileListSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = TeacherProfile
        fields = ('id', 'email', 'name', 'phone_number')


class TeacherProfileRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = ('id', 'email', 'name', 'phone_number')
