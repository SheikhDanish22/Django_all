from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    return render(request,'form.html')
    
def data(request):
    print(request.method)
    print(request.POST)
    print(request.FILES)


    A=request.POST.get('username')
    B=request.POST.get('email')
    C=request.POST.get('detail')
    D=request.POST.get('phone')
    E=request.POST.get('dob')
    F=request.POST.get('volume')
    G=request.POST.get('subscribe')
    H=request.POST.get('gender')
    I=request.FILES.get('profile-pic')
    J=request.FILES.get('resume')
    K=request.POST.get('password')
    L=request.POST.get('password')


    # user_data={'username':A,
    #            'email':B,
    #            'detail':C,
    #            'phone':D,
    #            'dob':E,
    #            'volume':F,
    #            'subscribe':G,
    #            'gender':H,
    #            'profile-pic':I,
    #            'resume':J,
    #            'password':K,
    #            'password':L,

    # }

    # print(A,B,C,D,E,F,G,H,I,J,K,L)
    # print(user_data)
    Student.objects.create( Name=A,Email=B,Description=C,Contect=D,DOB=E,Volume=F,Education=G,Gender=H,Image=I,Resume=J,Password=K,Con_Password=L)



