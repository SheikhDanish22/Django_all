from django.shortcuts import render
from app.models import Student
# Create your views here.

def alldata(request):
    data=Student.objects.all()
    print(data)


def fillterdata(request):
    data=Student.objects.filter(stu_name="sohan")
    print(data)  

def value(request):
    data=Student.objects.values()
    print(data)      

def vlist(request):
    data=Student.objects.values_list()
    print(data)

def ex(request):
    data=Student.objects.exclude(stu_name='Neeraj')
    print(data)    