import timeit

import logging
import logging.handlers
import os

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from functools import wraps

log = logging.getLogger(__name__)


def timer(func):
    """helper function to estimate view execution time"""

    @wraps(func)  # used for copying func metadata
    def wrapper(*args, **kwargs):
        # record start time
        start = timeit.default_timer()

        # func execution
        result = func(*args, **kwargs)

        duration = (timeit.default_timer() - start) * 1000

        if duration > 200:
            log.debug("This view takes more than 200ms to execute")
            log.debug(f"duration: {duration}")
        return result

    return wrapper


@method_decorator(csrf_exempt, name='dispatch')
class AddView(View):
    def get(self, request):
        start_time = timeit.default_timer()

        post = {"name": "Abdi", "score": 54}
        cluster = MongoClient(os.environ.get('MONGODB_URI_PYTHON'))
        db = cluster["test"]
        collection = db["PyMongoPractice"]
        difference = timeit.default_timer() - start_time

        if difference > 200:
            log.warning("This AddView takes more than 200ms to execute")

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
    # @timer
    def get(self, request):
        start_time = timeit.default_timer()
        cluster = MongoClient(os.environ.get('MONGODB_URI_PYTHON'))
        log.info("FindView...Connected successfully to the cluster. Time taken: {}".format(timeit.default_timer() - start_time))

        db = cluster["test"]
        collection = db["PyMongoPractice"]
        difference = timeit.default_timer() - start_time

        if difference > 0.2:
            log.warning(f"This FindView took {difference} seconds to connect to the database")

        # using find_one will return the first matching objects
        # for delete its delete_many({}) and delete_one({}) and so on

        log.info("Finding Name...")
        start_time = timeit.default_timer()
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
        difference = timeit.default_timer() - start_time
        log.info(f"It took {difference} seconds to find the data")
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
