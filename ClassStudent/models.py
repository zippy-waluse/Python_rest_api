from django.db import models

class Student(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    age = models.IntegerField()
    student_course = models. CharField()
    student_classroom = models.CharField()


    objects = models.Manager()
    def _str_ (self):
        return f"{self.first_name} {self.student_course}"




