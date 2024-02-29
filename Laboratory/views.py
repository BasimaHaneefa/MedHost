from django.shortcuts import render,redirect
from Admin.models import *
from Doctor.models import *
from User.models import *
from Guest.models import *
from .models import *

# Create your views here.

def homelaboratory(request):
    return render(request,'Laboratory/Home.html')

def labmyprofile(request):
    if 'lid' in request.session:
        myp=Laboratory.objects.get(id=request.session['lid'])
        return render(request,'Laboratory/Lab_Profile.html',{'seld':myp})
    else:    
        return redirect('guest:Login')

def uplabprofile(request,lid):
    if 'lid' in request.session:
        seld=Laboratory.objects.get(id=lid)
        if request.method=="POST":
            seld.name=request.POST.get('name')
            seld.address=request.POST.get('address')
            seld.contact=request.POST.get('contact')
            seld.email=request.POST.get('email')
            seld.save()
            return redirect('Laboratory:Lab_myprofile')
        return render(request,"Laboratory/Edit_Profile.html",{'User':seld})
    else:
        return redirect(request,'guest:Login')

def changelabpwd(request,lid):
    change=Laboratory.objects.get(id=lid)
    pwd=change.password
    if request.method=="POST":
        old=request.POST.get('current_pwd')
        if old!=pwd:
            Error="Password not correct"
            return render(request,'Laboratory/Change_password.html',{"error":Error})
        else:
            new=request.POST.get('new_password')
            change=Laboratory.objects.get(id=lid)
            change.password=new
            change.save()
            return redirect('guest:Login')
    else:
        return render(request,'Laboratory/Change_password.html')

def testdetails(request):
    tob=TestType.objects.all()
    if request.method=="POST":
        lab=Laboratory.objects.get(id=request.session['lid'])
        tid=request.POST.get('testtype')
        ttype=TestType.objects.get(id=tid)
        Testdetails.objects.create(name=request.POST.get('name'),test_amount=request.POST.get('test_amount'),
        test_details=request.POST.get('test_details'),testtype=ttype,laboratory=lab)
        selp=Testdetails.objects.all()
        return render(request,'Laboratory/TestDetails.html',{'test':tob,'ts':selp})
    else:
        selp=Testdetails.objects.all()
        return render(request,'Laboratory/TestDetails.html',{'test':tob,'ts':selp})

def viewcheckup(request):
    seld=Checkupdetails.objects.filter()
    return render(request,'Laboratory/View_Checkup.html',{'seld':seld})

def upcheckup(request,uid):
    seld=Checkupdetails.objects.get(id=uid)
    if request.method=="POST" and request.FILES:
        seld.checkup_result=request.FILES.get('checkup_result')
        seld.checkup_status=1
        seld.save()
        return redirect('Laboratory:viewcheckup')
    else:
        return render(request,'Laboratory/Edit_Checkup.html',{'result':seld})

def complaintlab(request):
    
    if request.method=="POST":
        lab=Laboratory.objects.get(id=request.session['lid'])
        Complaint.objects.create(title=request.POST.get('title'),content=request.POST.get('content'),Laboratory_id=lab)
        seld=Complaint.objects.filter(Laboratory_id=request.session['lid'])
        return render(request,'Laboratory/Complaint_Lab.html',{'seld':seld})
    else:
        seld=Complaint.objects.filter(Laboratory_id=request.session['lid'])
        return render(request,'Laboratory/Complaint_Lab.html',{'seld':seld})

def descriptionlab(request):    
    if request.method=="POST":
        lab=Laboratory.objects.get(id=request.session['lid'])
        Feedback.objects.create(description=request.POST.get('description'),Laboratory_id=lab)
        seld=Feedback.objects.filter(Laboratory_id=request.session['lid'])
        return render(request,'Laboratory/Description_lab.html',{'seld':seld})
    else:
        seld=Feedback.objects.filter(Laboratory_id=request.session['lid'])
        return render(request,'Laboratory/Description_lab.html',{'seld':seld})

        
def logout(request):
    if 'lid' in request.session:
        del request.session["lid"]
        return redirect("guest:Login")
    else:
        return redirect("guest:Login")
    