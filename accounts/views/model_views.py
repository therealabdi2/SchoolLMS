import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.core import serializers
from accounts.models import TeacherProfile


class TeacherListView(ListView):
    model = TeacherProfile

    # return a json response with all teachers
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = serializers.serialize("json", queryset)
        return JsonResponse(data, status=200, safe=False)


class TeacherDetailView(DetailView):
    model = TeacherProfile

    # return the specific teacher
    def get_queryset(self):
        queryset = super(TeacherDetailView, self).get_queryset()
        return queryset.filter(id=self.kwargs['id'])

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = serializers.serialize("json", queryset)
        # if data is empty return 404
        if not data:
            return JsonResponse({'message': 'Teacher not found'}, status=404)
        return JsonResponse(data, status=200, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class TeacherDeleteView(DeleteView):
    model = TeacherProfile

    def get_queryset(self):
        queryset = super(TeacherDeleteView, self).get_queryset()
        return queryset.filter(id=self.kwargs['id'])

    def delete(self, request, *args, **kwargs):
        # delete the teacher
        self.get_queryset().delete()
        return JsonResponse({'message': 'Teacher deleted'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class TeacherUpdateView(UpdateView):
    model = TeacherProfile

    def post(self, request, *args, **kwargs):
        # get the teacher from the database

        teacher = TeacherProfile.objects.get(id=self.kwargs['id'])
        put_body = json.loads(request.body)
        # update the teacher
        teacher.name = put_body['name']
        teacher.email = put_body['email']
        teacher.phone_number = put_body['phone_number']

        teacher.save()
        # return the updated teacher
        return JsonResponse(serializers.serialize("json", [teacher]), status=200, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class TeacherCreateView(CreateView):
    model = TeacherProfile
    fields = ['name', 'email', 'phone_number']

    def post(self, request, *args, **kwargs):
        # create the teacher
        post_body = json.loads(request.body)
        teacher = TeacherProfile(
            name=post_body['name'],
            email=post_body['email'],
            phone_number=post_body['phone_number']
        )

        teacher.save()
        # return the created teacher
        return JsonResponse(serializers.serialize("json", [teacher]), status=201, safe=False)
