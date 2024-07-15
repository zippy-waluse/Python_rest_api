from django.db import models

# Create your models here.

class Course(models.Model):
    course_id = models.SmallIntegerField()
    course_name = models.CharField(max_length=20)
    course_description = models.TextField()
    department = models.CharField(max_length=20)
    course_instructor = models.CharField(max_length=20)
    assessment_requirements = models.TextField()
    course_fee = models.IntegerField()


    def __str__(self):
         return f"{self.course_name}"