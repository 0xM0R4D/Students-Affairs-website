from decimal import MIN_ETINY
from pyexpat import model
from turtle import mode
from django.db import models

# Create your models here.


class stu(models.Model):
    stu_name=models.CharField(max_length=30)
    GPA=models.FloatField()
    stu_id=models.IntegerField(primary_key=True) 
    stu_dep=models.CharField(max_length=4)
    level=models.IntegerField()
    isActive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.stu_name
    
    class Meta:
        ordering=['stu_id']
    
class course(models.Model):
    course_name=models.CharField(max_length=30)
    course_hours = models.IntegerField()
    def __str__(self):
        return self.course_name
    
class coursestudent(models.Model):
    stuID = models.IntegerField()
    courseNAME=models.CharField(max_length=30)
    def __str__(self):
        return self.courseNAME
    
    class Meta:
        ordering=['stuID']
 