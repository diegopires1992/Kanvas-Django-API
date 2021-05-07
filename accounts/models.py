from django.db import models

from django.contrib.auth.models import User


class Courses(models.Model):
    name = models.CharField(max_length=255)
    user_set = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Activity(models.Model):
    repo = models.CharField(max_length=255)
    grade = models.IntegerField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)