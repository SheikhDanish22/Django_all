from django.db import models

# Create your models here.


class Aadhar(models.Model):
    aadhar_no = models.IntegerField(unique=True)
    created_by = models.CharField(max_length=50)
    date = models.DateField()
    def __str__(self):
        return str(self.aadhar_no)


class Userprofile(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Contact = models.IntegerField()
    Aadhar_no = models.OneToOneField(Aadhar,on_delete=models.PROTECT)
    def __str__(self):
        return self.Name

