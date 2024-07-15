from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Students
from .serializer import studentSerializer
from rest_framework.response import Response

# Create your views here.

class StudentListView(APIView):
    def get(self, request):
        students = Students.object.all()
        serializer = studentSerializer(students, many=True)
        return Response(serializer.data)