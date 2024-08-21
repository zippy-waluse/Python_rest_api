from rest_framework import serializers
from student.models import Students
from teacher.models import Teacher
from courses.models import Course
from classperiod.models import Period
from teacher.models import  Teacher
from classes.models import Classes

class MinimalStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['first_name', 'email']

# class StudentSerializer(serializers.ModelSerializer):
#     teacher = MinimalTeacherSerializerr()
#     class Meta:
#         model = Students
#         fields = '__all__'
 
class MinimalTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name', 'email']

class TeacherSerializer(serializers.ModelSerializer):
    courses = CoursesSerializer(many=True)
    class Meta:
        model = Teacher
        fields = '__all__'

class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'description']

class CourseSerializer(serializers.ModelSerializer):
    periods = ClassesSerializer(many=True)
    class Meta:
        model = Course
        fields = '__all__'

class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ['time', 'day']

class ClassPeriodSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    course = CourseSerializer()
    class Meta:
        model = Period
        fields = '__all__'

class MinimalClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['name', 'description']

class ClassesSerializer(serializers.ModelSerializer):
    students = MinimalStudentSerializer(many=True)
    periods = ClassPeriodSerializer(many=True)
    class Meta:
        model = Classes
        fields = '__all__'