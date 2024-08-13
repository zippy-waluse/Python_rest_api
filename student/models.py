from django.db import models
from courses.models import Course
# from django.db.models.manager import BaseManager

# Create your models here.

class Students(models.Model):
    courses = models.ManyToManyField(Course) 
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    code = models.PositiveBigIntegerField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=20)
    bio = models.TextField()

    # objects: BaseManager['Student']
    
    objects = models.Manager()
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    



    
