import json

from accounts.models import TeacherProfile

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from faker import Faker


@method_decorator(csrf_exempt, name='dispatch')
class TeacherView(View):
    def get(self, request):
        """
        This function returns a json object with list of teachers.
        The json object contains a list of teachers and the count of teachers.
        The list of teachers contains the following information:
        - teacher_id
        - teacher_name
        - teacher_email
        - teacher_phone
        :param request:
        :return:
        """
        teachers = TeacherProfile.objects.all()
        teacher_count = len(teachers)
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
        """
                This function creates a new teacher profile.
                It takes in the following parameters:
                name: The name of the teacher
                email: The email of the teacher
                phone_number: The phone number of the teacher
                It returns the following:
                A JSON response with the following keys:
                message: A message indicating the success of the operation
                :param request:
                :return:
        """
        post_body = json.loads(request.body)

        teacher_name = post_body.get('name')
        teacher_email = post_body.get('email')
        teacher_phone = post_body.get('phone_number')

        # check if teacher email already exists
        if TeacherProfile.objects.filter(email=teacher_email).exists():
            return JsonResponse({'error': 'Teacher with this email already exists'}, status=400)

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
class AddFakeData(View):
    def post(self, request):
        fake = Faker()

        teacher_data = {
            'name': fake.name(),
            'email': fake.email(),
            'phone_number': fake.phone_number(),
        }

        teacher_obj = TeacherProfile.objects.create(**teacher_data)
        data = {
            'message': f'New Teacher profile has been created with id {teacher_obj.id}'

        }
        return JsonResponse(data, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class TeacherRetrieveUpdateDeleteView(View):
    def get(self, request, teacher_id):
        """
        This function returns a json object with a teacher profile.
        The json object contains the following information:
        - teacher_id
        - teacher_name
        - teacher_email
        - teacher_phone
        :param request:
        :param teacher_id:
        :return:
        """
        try:
            teacher = TeacherProfile.objects.get(pk=teacher_id)
            data = {
                'teacher_id': teacher.pk,
                'teacher_name': teacher.name,
                'teacher_email': teacher.email,
                'teacher_phone': teacher.phone_number,
            }
            return JsonResponse(data, status=200)
        except TeacherProfile.DoesNotExist:
            return JsonResponse({'error': 'Teacher does not exist'}, status=404)

    def put(self, request, teacher_id):
        """
        This function updates the name of the teacher with the given id.
        It takes in the request body and updates the name of the teacher.
        It returns a message with the id of the teacher whose name has been updated.
        :param request:
        :param teacher_id:
        :return:
        """
        try:
            teacher = TeacherProfile.objects.get(id=teacher_id)
            # getting the data from our request body
            put_body = json.loads(request.body)
            teacher.name = put_body.get('name')
            teacher.save()

            data = {
                'message': f'Name of the teacher with id {teacher_id} has been updated'
            }
            return JsonResponse(data, status=200)
        except TeacherProfile.DoesNotExist:
            data = {
                'message': f'Teacher Profile with id {teacher_id} does not exist'
            }
            return JsonResponse(data, status=404)

    def delete(self, request, teacher_id):
        """
        This function deletes a teacher profile from the database.
        It takes in the request and the teacher_id as parameters.
        It gets the teacher profile object from the database and deletes it.
        If the object does not exist, it returns a not found error.
        :param request:
        :param teacher_id:
        :return:
        """

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
