from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
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

image = face_recognition.load_image_file("your_file.jpg")
face_locations = face_recognition.face_locations(image)

class EmployeesRegistrationView(viewsets.CreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

class EmployeesRecognitionView(APIView):
    def post(self, request, format=None):
        picture_of_me = face_recognition.load_image_file("me.jpg")
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

        # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

        unknown_picture = face_recognition.load_image_file("unknown.jpg")
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

        # Now we can see the two face encodings are of the same person with `compare_faces`!

        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

        if results[0] == True:
            print("It's a picture of me!")
        else:
            print("It's not a picture of me!")








