import json

from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from accounts.models import TeacherProfile


@method_decorator(csrf_exempt, name='dispatch')
class TeacherView(View):
    def get(self, request):
        # return a json object with list of teachers
        teacher_count = TeacherProfile.objects.count()
        teachers = TeacherProfile.objects.all()

        teachers_serialized_data = []
        for teacher in teachers:
            teachers_serialized_data.append({
                'teacher_id': teacher.pk,
                'teacher_name': teacher.name,
                'teacher_email': teacher.email,
                'teacher_phone': teacher.phone_number,
            })

        data = {
            'teachers': teachers_serialized_data,
            'count': teacher_count,
        }
        return JsonResponse(data, status=200)

        # if request.user.is_superuser:
        #     teacher_as_json = serializers.serialize('json', TeacherProfile.objects.all())
        #     return HttpResponse(teacher_as_json, content_type='application/json', status=200)
        # return JsonResponse({'error': 'Only superuser can view all teachers'}, status=403)

    def post(self, request):
        post_body = json.loads(request.body)

        teacher_name = post_body.get('name')
        teacher_email = post_body.get('email')
        teacher_phone = post_body.get('phone_number')

        # check if teacher email already exists
        if TeacherProfile.objects.filter(email=teacher_email).exists():
            return JsonResponse({'error': 'Teacher with email already exists'}, status=400)

        teacher_data = {
            'name': teacher_name,
            'email': teacher_email,
            'phone_number': teacher_phone,
        }

        # if any of the fields is missing, return error
        if not all(teacher_data.values()):
            return JsonResponse({'error': 'All fields are required'}, status=400)

        teacher_obj = TeacherProfile.objects.create(**teacher_data)
        data = {
            'message': f'New Teacher profile has been created with id {teacher_obj.id}'
        }
        return JsonResponse(data, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class TeacherUpdateDeleteView(View):
    def put(self, request, teacher_id):
        teacher = TeacherProfile.objects.get(id=teacher_id)
        # getting the data from our request body
        put_body = json.loads(request.body)
        teacher.name = put_body.get('name')
        teacher.save()

        data = {
            'message': f'Name of the teacher with id {teacher_id} has been updated'
        }
        return JsonResponse(data, status=200)

    def delete(self, request, teacher_id):
        # get the object from DB and delete it if object does not exist return a not found error
        try:
            teacher = TeacherProfile.objects.get(id=teacher_id)
            teacher.delete()
            data = {
                'message': f'Teacher Profile with id {teacher_id} has been deleted'
            }
            return JsonResponse(data, status=200)

        except TeacherProfile.DoesNotExist:
            data = {
                'message': f'Teacher Profile with id {teacher_id} does not exist'
            }
            return JsonResponse(data, status=404)
