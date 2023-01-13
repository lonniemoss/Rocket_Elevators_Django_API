from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapi.serializers import EmployeesSerializer
from myapi.models import Employees
from rest_framework import generics
import face_recognition

@api_view(['GET'])
def getData(request):
    employees = Employees.objects.all()
    serializer = EmployeesSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_employee_photo(request, employee_id):
    try:
        employee = Employees.objects.get(id=employee_id)
    except Employees.DoesNotExist:
        return Response("Employee not found")
    image_file = request.FILES.get('image')
    if not image_file:
        return Response("No image provided")
    image = face_recognition.load_image_file(image_file)
    face_encoding = face_recognition.face_encodings(image)[0]
    employee.facial_keypoints = face_encoding.tolist()
    employee.save()
    return Response("Facial keypoints added successfully")

@api_view(['POST'])
def add_employee(request):
    serializer = EmployeesSerializer(data=request.data)
    if serializer.is_valid():
        employee = serializer.save()
        image_file = request.FILES.get('image')
        if image_file:
            image = face_recognition.load_image_file(image_file)
            face_encoding = face_recognition.face_encodings(image)[0]
            employee.facial_keypoints = face_encoding.tolist()
            employee.save()
        return  Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
def recognize_employee(request):
    image_file = request.FILES.get('image')
    if not image_file:
        return Response("No image provided")
    image = face_recognition.load_image_file(image_file)
    face_encoding = face_recognition.face_encodings(image)[0]
    matches = Employees.objects.filter(facial_keypoints__contains=face_encoding.tolist())
    if matches.exists():
        employee = matches.first()
        serializer = EmployeesSerializer(employee)
        return Response(serializer.data)
    else:
        return Response("Employee not found.")



