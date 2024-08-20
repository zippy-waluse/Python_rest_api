from student.models import Students
from rest_framework import serializers
from teacher.models import Teacher
from courses.models import Course
from classperiod.models import Period
from classes.models import Classes


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
         model = Students
         fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
         model = Teacher
         fields = '__all__'


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
         model = Course
         fields = '__all__'


class ClassperiodSerializer(serializers.ModelSerializer):
    class Meta:
         model = Period
         fields = '__all__'

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
         model = Classes
         fields = '__all__'      

class MinimalSerializer(serializers.ModelSerializer):
     class Meta:
          model= Students
          fields = ["first_name","email"]            