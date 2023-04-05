from django.db import models
from datetime import datetime

# create your models here.

class usersignup(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()

class mynotes(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    email=models.EmailField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)    
    myfile=models.FileField(upload_to='Uploaded_Files')

    
class feedback(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    msg=models.TextField()