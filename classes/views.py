import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from accounts.models import TeacherProfile
from classes.models import ClassGrade


@method_decorator(csrf_exempt, name='dispatch')
class ClassView(View):
    def get(self, request):
        class_count = ClassGrade.objects.count()
        classes = ClassGrade.objects.all()

        classes_serialized_data = []
        for some_class in classes:
            classes_serialized_data.append({
                'class_id': some_class.pk,
                'class_teachers': [x.as_dict() for x in some_class.teacher.all()],
                'class_name': some_class.name,
                'class_img': some_class.image.url,
            })

        data = {
            'classes': classes_serialized_data,
            'count': class_count,
        }
        return JsonResponse(data, status=200)

    def post(self, request):
        post_body = json.loads(request.body)
        print(post_body)
        class_name = post_body.get('class_name')
        class_img = post_body.get('class_img')

        if ClassGrade.objects.filter(name=class_name).exists():
            return JsonResponse({'message': 'Class with this name already exists'}, status=400)

        class_data = {
            'name': class_name,
            'image': class_img,
        }

        if not all(class_data.values()):
            return JsonResponse({'error': 'All fields are required'}, status=400)

        class_obj = ClassGrade.objects.create(**class_data)

        data = {
            'message': 'New class created successfully!',
        }
        return JsonResponse(data, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class AssignTeacherView(View):
    def post(self, request, pk):
        # check if class exists
        if not ClassGrade.objects.filter(pk=pk).exists():
            return JsonResponse({'message': 'Class does not exist'}, status=400)

        post_body = json.loads(request.body)
        teacher_ids = post_body.get('class_teachers')

        if not teacher_ids:
            return JsonResponse({'error': 'Teacher id is required'}, status=400)

        # find the teacher ids
        teachers = []
        for teacher_id in teacher_ids:
            teacher = TeacherProfile.objects.get(pk=teacher_id["pk"])
            teachers.append(teacher)

        print(teachers)

        # assign teachers
        class_obj = ClassGrade.objects.get(pk=pk)
        class_obj.teacher.set(teachers)

        data = {
            'message': 'Teacher(s) assigned successfully!',
        }
        return JsonResponse(data, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class ClassRetrieveUpdateDeleteView(View):
    def get(self, request, class_id):
        pass
