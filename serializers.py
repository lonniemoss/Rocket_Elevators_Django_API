from rest_framework import serializers
from .models import *

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('id', 'title', 'firstname', 'lastname', 'email', 'password', 'created_at', 'updated_at', 'facial_keypoints')

