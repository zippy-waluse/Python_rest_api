from student.models import Students
from rest_framework import serializers



class studentSerializer(serializers.ModelSerializer):
    class Meta:
         model = Students
         fields = '__all__'