from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from api import serializer
from student.models import Students
from rest_framework import status
from student.models import ClassStudent
from teacher.models import Teacher
from courses.models import Course
from classperiod.models import Period
from api.serializer import MinimalStudentSerializer, StudentSerializer, Student_ClassSerializer, TeacherSerializer, CourseSerializer, Class_PeriodSerializer, MinimalTeacherSerializer, MinimalStudent_ClassSerializer, MinimalCourseSerializer, MinimalClass_PeriodSerializer
class StudentListView(APIView):
    def get(self, request):
        students = ClassStudent.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            students=students.filter(first_name=first_name)
        country = request.query_params.get("country")
        if country:
            Students = ClassStudent.filter(country = country)
        serializer = StudentSerializer(students, many =True)
        serializer = MinimalStudentSerializer(students, many =True)
        return Response(serializer.data)
    def post(self, request):
        serializer = StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class StudentDetailView(APIView):
    def get(self, request, id):
        student=ClassStudent.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    def put(self, request, id):
        student = ClassStudent.objects.get(id=id)
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        student = ClassStudent.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    def enroll(self, student, course_id):
        course = Course.objects.get(id=course_id)
        student.courses.add(course)
    def unenroll(self, student, course_id):
        course = Course.objects.get(id=course_id)
        student.courses.remove(course)
    def add_to_class(self, student, class_id):
        student_class = ClassStudent.objects.get(id=class_id)
        student_class.students.add(student)
    def post(self, request, id):
        student= ClassStudent.objects.get(id=id)
        action = request.data.get("action")
        if action =="enroll":
            course_id = request.data.get("course_id")
            self.enroll(student, course_id)
            return Response(status=status.HTTP_201_CREATED)
        elif action == "unenroll":
            course_id = request.data.get("course_id")
            self.unenroll(student, course_id)
            return Response(status=status.HTTP_200_OK)
        elif action == "add_to_class":
            class_id = request.data.get("class_id")
            self.add_to_class(student, class_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
         return Response(status=status.HTTP_400_BAD_REQUEST)
class Student_ClassListView(APIView):
    def get(self, request):
        student_class = ClassStudent.objects.all()
        serializer = Student_ClassSerializer(student_class, many=True)
        serializer = MinimalStudent_ClassSerializer(student_class, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = Student_ClassSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Student_ClassDetailView(APIView):
    def get(self, request, id):
        student_class= ClassStudent.objects.get(id=id)
        serializer = Student_ClassSerializer(student_class)
        return Response(serializer.data)
    def put(self, request, id):
        student_class = ClassStudent.objects.get(id=id)
        serializer = StudentSerializer(student_class, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        student_class = ClassStudent.objects.get(id=id)
        student_class.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        serializer = MinimalTeacherSerializer(teachers, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TeacherSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher= ClassStudent.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    def assign_course(self, teacher, course_id):
        course = Course.objects.get(id=course_id)
        teacher.courses.add(course)
    def assign_class(self, teacher, class_id):
        student_class = ClassStudent.objects.get(id=class_id)
        student_class.teacher = teacher
        student_class.save()
    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign_course":
            course_id = request.data.get("course_id")
            self.assign_course(teacher, course_id)
            return Response(status=status.HTTP_201_CREATED)
        elif action == "assign_class":
            class_id = request.data.get("class_id")
            self.assign_class(teacher, class_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        serializer = MinimalCourseSerializer(courses, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CourseSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CourseDetailView(APIView):
    def get(self, request, id):
        course= Course.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    def put(self, request, id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
class Class_PeriodListView(APIView):
    def get(self, request):
        class_period = Period.objects.all()
        serializer = Class_PeriodSerializer(class_period, many=True)
        serializer = MinimalClass_PeriodSerializer(class_period, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = Class_PeriodSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Class_PeriodDetailView(APIView):
    def get(self, request, id):
        class_period= Period.objects.get(id=id)
        serializer = Class_PeriodSerializer(class_period)
        return Response(serializer.data)
    def put(self, request, id):
        class_period = Period.objects.get(id=id)
        serializer = StudentSerializer(class_period, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        class_period = Period.objects.get(id=id)
        class_period.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    def post(self, request, id):
        action = request.data.get("action")
        if action == "create_class_period":
            teacher_id = request.data.get("teacher_id")
            course_id = request.data.get("course_id")
            self.create_class_period(teacher_id, course_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def create_class_period(self, teacher_id, course_id):
        teacher = Teacher.objects.get(id=teacher_id)
        course = Course.objects.get(id=course_id)
        class_period = Period(teacher=teacher, course=course)
        class_period.save()
        return Response(status=status.HTTP_201_CREATED)