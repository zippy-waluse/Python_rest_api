from django.db import models
class ClassDuration(models.Model):


   class_name = models.CharField(max_length=40)
   class_id = models.SmallIntegerField()
   course_description = models.CharField(max_field=20)
   trainer = models.CharField()
   start_time = models.TimeField()
   end_time = models.TimeField()
   date = models.DateField()


   def _str_(self):
      return f"{self.class_name}{self.class_id}"
