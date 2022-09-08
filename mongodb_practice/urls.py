from django.urls import path

from mongodb_practice.views import AddView, InsertManyView, FindView, UpdateStuffView

app_name = 'mongodb_practice'

urlpatterns = [
    path('add-view/', AddView.as_view()),
    path('insert-many/', InsertManyView.as_view()),
    path('find-stuff/', FindView.as_view()),
    path('update-stuff/', UpdateStuffView.as_view()),


]
