from django.db import models

# Create your models here.]

class Student(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Description=models.CharField(max_length=50)
    Contect=models.IntegerField()
    DOB=models.DateField()
    Volume=models.IntegerField()
    Education=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Image=models.ImageField()
    Resume=models.FileField()
    Password=models.CharField(max_length=50)
    Con_Password=models.CharField(max_length=50)

