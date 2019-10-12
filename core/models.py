from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    job = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    education = models.CharField(max_length=300)
    skills = models.CharField(max_length=1000)
    experience = models.TextField(max_length=2000)

class Activity(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    data = models.TextField(max_length=2000)
    date = models.DateTimeField()