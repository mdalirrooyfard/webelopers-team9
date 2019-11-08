from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    department = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    course_number = models.CharField(max_length=300)
    group_number = models.CharField(max_length=300)
    teacher = models.CharField(max_length=300)
    choices = [(1,'saturday'),(2,'sunday'),(3,'monday'),(4,'tuesday'),(5,'wednesday')]
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = models.IntegerField(choices=choices)
    second_day = models.IntegerField(choices=choices,null=True, blank=True)

