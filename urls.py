from django.urls import path
from django.contrib import admin
from django.urls import path, include
from myapi.views import EmployeesRegistrationView, EmployeesRecognitionView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', EmployeesRegistrationView.as_view(), name='employee-registration'),
    path('recognize/', EmployeesRecognitionView.as_view(), name='employee-recognition'),
]

