import pymongo
import os

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient


@method_decorator(csrf_exempt, name='dispatch')
class AddView(View):
    def get(self, request):
        post = {"name": "Abdi", "score": 54}
        cluster = MongoClient(os.environ.get('MONGODB_URI_PYTHON'))
        db = cluster["test"]
        collection = db["PyMongoPractice"]
        collection.insert_one(post)
        data = {
            'message': 'Data added successfully'
        }
        return JsonResponse(data, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class InsertManyView(View):
    def get(self, request):
        post1 = {"name": "Ali", "score": 22}
        post2 = {"name": "Abid", "score": 18}

        cluster = MongoClient(os.environ.get('MONGODB_URI_PYTHON'))
        db = cluster["test"]
        collection = db["PyMongoPractice"]
        collection.insert_many([post1, post2])

        data = {
            'message': 'Data added successfully'
        }
        return JsonResponse(data, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class FindView(View):
    def get(self, request):
        cluster = MongoClient(os.environ.get('MONGODB_URI_PYTHON'))
        db = cluster["test"]
        collection = db["PyMongoPractice"]

        # using find_one will return the first matching objects
        # for delete its delete_many({}) and delete_one({}) and so on

        results = collection.find({"name": "Ali"})
        serialized_data = []
        for result in results:
            serialized_data.append({
                "name": result["name"],
                "score": result["score"]
            })
        print(serialized_data)
        data = {
            'Found': serialized_data
        }
        return JsonResponse(data, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class UpdateStuffView(View):
    def get(self, request):
        cluster = MongoClient(os.environ.get('MONGODB_URI_PYTHON'))
        db = cluster["test"]
        collection = db["PyMongoPractice"]
        results = collection.update_one({"name": "Abdi"}, {"$set": {"score": 100}})
        data = {
            "Success": "Data updated!"
        }
        return JsonResponse(data, status=201)
