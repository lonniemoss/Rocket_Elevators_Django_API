from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import generics
from .serializers import EmployeesSerializer
from .models import Employees
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import face_recognition
import numpy as np
from PIL import Image
import io
import base64

image = face_recognition.load_image_file("myapi/images/profile_pic.jpg")
face_locations = face_recognition.face_locations(image)

class EmployeesRegistrationView(generics.CreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

class EmployeesRecognitionView(APIView):
    def post(self, request, format=None):
        image = request.data['image']
        image = Image.open(io.BytesIO(base64.b64decode(image)))
        image = np.array(image)
        image = face_recognition.load_image_file(image)
        face_locations = face_recognition.face_locations(image)

        employees = Employees.objects.all()
        for employee in employees:
            employee_image = face_recognition.load_image_file(employee.image)
            employee_face_locations = face_recognition.face_locations(employee_image)
            employee_face_encoding = face_recognition.face_encodings(employee_image, employee_face_locations)[0]
            results = face_recognition.compare_faces([employee_face_encoding], image)
            if results[0]:
                return Response({
                    'message': 'Employee recognized',
                    'employee': {
                        'id': employee.id,
                        'first_name': employee.first_name,
                        'last_name': employee.last_name,
                        'role': employee.role,
                        'email': employee.email,
                        'phone': employee.phone,
                        'image': employee.image
                    }
                }, status=status.HTTP_200_OK)

        return Response({
            'message': 'Employee not recognized'
        }, status=status.HTTP_404_NOT_FOUND)








