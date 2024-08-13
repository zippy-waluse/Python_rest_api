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
from rest_framework import status

from rest_framework.response import Response


# Create your views here.

class StudentListView(APIView):
    def get(self, request):
        students = Students.objects.all()
        first_name = request.query_params.get("first_name")
        country = request.query_params.get("country")
        if first_name:
            students = students.filter(first_name = first_name)
        if country:
            students=students.filter(country=country)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

        
    
    
class StudentDetailView(APIView):
    def get(self,request,id):
        courses=Students.objects.get(id=id)
        serializer =CoursesSerializer(courses)
        return Response(serializer.data)
    
    def put(self, request,id):
       student=Students.objects.get()(id=id)
       serializer =StudentSerializer(student,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
    def delete(self,request,id):
        student=Students.objects.get(id=id)
        serializer =StudentSerializer(student)
        student.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)    
    
    def enroll_student(student,course_id):
        Course=Course.objects.get(id=course_id)
        student.course.add(Course)

    def post(self,request,id):
        Students=Students.objects.get(id=id)
        action = request.data.get("action")
        if action== "enroll":
           course_id=request.data.get("course")
           self.enroll_student(Students,course_id)
        return Response(status.HTTP_201_ACCEPTED)       


class TeacherListView(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class TeacherDetailView(APIView):
    def get(self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer =TeacherSerializer(teacher)
        return Response(serializer.data)
    def put(self, request,id):
       teacher=Teacher.objects.get(id=id)
       serializer =TeacherSerializer(teacher,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer =TeacherSerializer(teacher)
        teacher.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)




class ClassesListView(APIView):
    def get(self, request):
        classes = Classes.objects.all()
        serializer = ClassesSerializer(classes, many=True)
        return Response(serializer.data)
    
    
    

    def post(self, request):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ClassesDetailView(APIView):
    def get(self,request,id):
        classe=Classes.objects.get(id=id)
        serializer =ClassesSerializer(classe)
        return Response(serializer.data)
    def put(self, request,id):
       classe=Classes.objects.get(class_id=id)
       serializer =ClassesSerializer(classe,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        classe=Classes.objects.get(id=id)
        serializer =ClassesSerializer(classe)
        classe.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)


class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class CoursesDetailView(APIView):
    def get(self,request,id):
        courses=Course.objects.get(id=id)
        serializer =CoursesSerializer(courses)
        return Response(serializer.data)
    def put(self, request,id):
       courses=Course.objects.get(id=id)
       serializer =CoursesSerializer(courses,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        courses=Course.objects.get(id=id)
        serializer =CoursesSerializer(courses)
        courses.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)



class ClassperiodListView(APIView):
    def get(self, request):
        period = Period.objects.all()
        serializer = ClassperiodSerializer(period, many=True)
        return Response(serializer.data)
    
    def put(self, request,id):
       period=Period.objects.get(class_id=id)
       serializer =ClassperiodSerializer(period,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
class Class_PeriodDetailView(APIView):
    def get(self,request,id):
        period=Period.objects.get(id=id)
        serializer =ClassesSerializer(period)
        return Response(serializer.data)
    
    def delete(self,request,id):
        period=Period.objects.get(id=id)
        serializer =ClassperiodSerializer(period)
        period.delete()
        return Response(serializer.errors,status=status.HTTP_202_ACCEPTED)





