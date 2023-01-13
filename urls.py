from django.urls import path
from django.contrib import admin
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('employee/<int:employee_id>/photo', views.add_employee_photo),
    path('recognize', views.recognize_employee),
    path('list', views.getData),
    path('employee', views.add_employee)
]

