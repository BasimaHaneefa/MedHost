from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from .models import *

# Create your views here.
def userregistration(request):
    disob=District.objects.all()
    if request.method=="POST" and request.FILES:
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        
        plcid=request.POST.get('place')
        plc=Place.objects.get(id=plcid)
        if password==cpassword:
            UserRegistration.objects.create(name=request.POST.get('name'),contact=request.POST.get('contact'),
            email=request.POST.get('email'),address=request.POST.get('address'),
            gender=request.POST.get('gender'),photo=request.FILES.get('image'),proof=request.FILES.get('proof'),
            place=plc,password=password)

        return render(request,'Guest/UserRegistration.html',{'Dis':disob})
    else:
        return render(request,'Guest/UserRegistration.html',{'Dis':disob})

def ajaxplc(request):
    dist=request.GET.get('district')
    plc=Place.objects.filter(district=dist)
    return render(request,"Guest/AjaxPlace.html",{'PLC':plc})

def login(request):
    if request.method=="POST":
        Email=request.POST.get('email')
        Password=request.POST.get('password')
        User=UserRegistration.objects.filter(email=Email,password=Password,u_status=True).count()
        Doctor=DoctorReg.objects.filter(email=Email,password=Password).count()
        Lab=Laboratory.objects.filter(email=Email,password=Password).count()
        Admin=AdminLogin.objects.filter(email=Email,password=Password).count()
        if User > 0:
            user=UserRegistration.objects.get(email=Email,password=Password,u_status=1)
            request.session["uid"]=user.id
            return redirect('user:homepage')
        elif Doctor > 0:
            doctor=DoctorReg.objects.get(email=Email,password=Password)
            request.session["did"]=doctor.id
            return redirect('doctor:Home_Doctor')
        elif Lab > 0:
            lab=Laboratory.objects.get(email=Email,password=Password)
            request.session["lid"]=lab.id
            return redirect('Laboratory:Home_Lab')
        elif Admin > 0:
            admin=AdminLogin.objects.get(email=Email,password=Password)
            request.session["aid"]=admin.id
            return redirect('webadmin:home')
        else:
            error="Invalid Credentials!!!"
            return render(request,"Guest/Login.html",{'Error':error})
    else:       
        return render(request,'Guest/Login.html')

def index(request):
    return render(request,'Guest/index.html')


