from datetime import date, datetime
from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Doctor.models import *
from .models import *
# Create your views here.
def homepage(request):
    return render(request,'User/Home.html')

def myprofile(request):
    if 'uid' in request.session:
        myp=UserRegistration.objects.get(id=request.session['uid'])
        return render(request,'User/MyProfile.html',{'seld':myp})
    else:    
        return redirect('guest:Login')

def upprofile(request,uid):
    if 'uid' in request.session:
        seld=UserRegistration.objects.get(id=uid)
        if request.method=="POST":
            seld.name=request.POST.get('name')
            seld.address=request.POST.get('address')
            seld.contact=request.POST.get('contact')
            seld.email=request.POST.get('email')
            seld.save()
            return redirect('user:myprofile')
        return render(request,"User/EditProfile.html",{'User':seld})
    else:
        return redirect(request,'guest:Login')

def changepwd(request,uid):
    change=UserRegistration.objects.get(id=uid)
    pwd=change.password
    if request.method=="POST":
        old=request.POST.get('current_pwd')
        if old!=pwd:
            Error="Password not correct"
            return render(request,'User/ChangePassword.html',{"error":Error})
        else:
            new=request.POST.get('new_password')
            change=UserRegistration.objects.get(id=uid)
            change.password=new
            change.save()
            return redirect('guest:Login')
    else:
        return render(request,'User/ChangePassword.html')
    

def searchdoctor(request):
    disob=Department.objects.all()
    if request.method=="POST":
        disid=request.POST.get('department')
        dis=Department.objects.get(id=disid)
        seld=DoctorReg.objects.all()
        return render(request,'User/SearchDoctor.html',{'dep':disob,'seld':seld})
    else:
        seld=DoctorReg.objects.all()
        return render(request,'User/SearchDoctor.html',{'dep':disob,'seld':seld})

def getdoctor(request):
    dept=request.GET.get('department')
    doc=DoctorReg.objects.filter(department=dept)
    return render(request,'User/GetDoctor.html',{'Doc':doc})

def appoinmet(request,did):
    doc=DoctorReg.objects.get(id=did)
    user=UserRegistration.objects.get(id=request.session['uid'])
    mydate=datetime.now()
    solts=Slots.objects.filter(doctor_id=doc,slot_status=0,slot_date__gt=mydate)
    return render(request,'User/Appoinment.html',{'res':solts})

def viewprescription(request):
        
    seld=Prescription.objects.filter(appoinment_id=request.session['appo'])
    return render(request,'User/View_prescription.html',{'seld':seld})

def complaint(request):
    
    if request.method=="POST":
        user=UserRegistration.objects.get(id=request.session['uid'])
        Complaint.objects.create(title=request.POST.get('title'),content=request.POST.get('content'),User_id=user)
        seld=Complaint.objects.filter(User_id=request.session['uid'])
        return render(request,'User/Complaint_User.html',{'seld':seld})
    else:
        seld=Complaint.objects.filter(User_id=request.session['uid'])
        return render(request,'User/Complaint_User.html',{'seld':seld})

def description(request):
    
    if request.method=="POST":
        user=UserRegistration.objects.get(id=request.session['uid'])
        Feedback.objects.create(description=request.POST.get('description'),User_id=user)
        seld=Feedback.objects.filter(User_id=request.session['uid'])
        return render(request,'User/Description.html',{'seld':seld})
    else:
        seld=Feedback.objects.filter(User_id=request.session['uid'])
        return render(request,'User/Description.html',{'seld':seld})
    

def Bookappoinmet(request,did):
    slot=Slots.objects.get(id=did)
    did=slot.doctor_id
    
    user=UserRegistration.objects.get(id=request.session['uid'])
    dat=slot.slot_date
    count=Appoinment.objects.filter(User_id=user,for_date=dat,slot_id__doctor_id=did).count()
    if count<=0:
        Appoinment.objects.create(for_date=dat,slot_id=slot,User_id=user)
        slot.slot_status=1
        slot.save()
        return redirect('user:homepage')
    else:
        return redirect('user:homepage')

def myappoinment(request):
    user=UserRegistration.objects.get(id=request.session['uid'])
    selp=Appoinment.objects.filter(User_id=user)
    return render(request,'User/My_Appoinment.html',{'res':selp})

def paynow(request,aid):
    request.session['appo']=aid
    if request.method=="POST":
       return redirect('user:viewprescription') 
    return render(request,'User/Payment.html')


def logout(request):
    if 'uid' in request.session:
        del request.session["uid"]
        return redirect("guest:Login")
    else:
        return redirect("guest:Login")

