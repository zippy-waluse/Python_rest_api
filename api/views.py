from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Students
from teacher.models import Teacher
from classes.models import Classes
from courses.models import Course
from classperiod.models import Period
from .serializer import StudentSerializer
from .serializer import TeacherSerializer
from .serializer import ClassperiodSerializer
from .serializer import ClassesSerializer
from .serializer import CoursesSerializer

from rest_framework.response import Response


# Create your views here.

class StudentListView(APIView):
    def get(self, request):
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    

class TeacherListView(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
    
    


class ClassesListView(APIView):
    def get(self, request):
        classes = Classes.objects.all()
        serializer = ClassesSerializer(classes, many=True)
        return Response(serializer.data)
    



class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data)
    


class ClassperiodListView(APIView):
    def get(self, request):
        period = Period.objects.all()
        serializer = ClassperiodSerializer(period, many=True)
        return Response(serializer.data)
    
