from django.db import models

# Create your models here.


# class Aadhar(models.Model):
#     aadhar_no = models.IntegerField(unique=True)
#     created_by = models.CharField(max_length=50)
#     date = models.DateField()
#     def __str__(self):
#         return str(self.aadhar_no)


# class Userprofile(models.Model):
#     Name = models.CharField(max_length=50)
#     Email = models.EmailField(unique=True)
#     Contact = models.IntegerField()
#     Aadhar_no = models.OneToOneField(Aadhar,on_delete=models.PROTECT)
#     def __str__(self):
#         return self.Name

class Department(models.Model):
    dep_name=models.CharField(max_length=50,unique=True)
    dep_des=models.TextField()
    dep_had=models.CharField(max_length=50)
    def __str__(self):
        return self.dep_name
    

class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_dep=models.ForeignKey(Department,on_delete=models.PROTECT,to_field='dep_name')
    stu_roll=models.CharField(max_length=50)
    def __str__(self):
        return str (self.stu_name   ) 