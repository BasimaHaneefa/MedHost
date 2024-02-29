from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from Guest.models import *
from Laboratory.models import *
from .models import *

def homedoctor(request):
    return render(request,'Doctor/home.html')

def doctorprofile(request):
    if 'did' in request.session:
        myp=DoctorReg.objects.get(id=request.session['did'])
        return render(request,'Doctor/DoctorProfile.html',{'seld':myp})
    else:    
        return redirect('guest:Login')

def updocprofile(request,drid):
    if 'did' in request.session:
        seld=DoctorReg.objects.get(id=drid)
        if request.method=="POST":
            seld.name=request.POST.get('name')
            seld.address=request.POST.get('address')
            seld.contact=request.POST.get('contact')
            seld.email=request.POST.get('email')
            seld.experience=request.POST.get('experience')
            seld.save()
            return redirect('doctor:Doctor_Profile')
        else:
            return render(request,'Doctor/EditProfile.html',{'User':seld})
    else:
        return redirect(request,'guest:Login')

def changepwd(request,uid):
    change=DoctorReg.objects.get(id=uid)
    pwd=change.password
    if request.method=="POST":
        old=request.POST.get('current_pwd')
        if old!=pwd:
            Error="Password not correct"
            return render(request,'Doctor/Change_Password.html',{"error":Error})
        else:
            new=request.POST.get('new_password')
            change=DoctorReg.objects.get(id=uid)
            change.password=new
            change.save()
            return redirect('guest:Login')
    else:
        return render(request,'Doctor/Change_Password.html')

def accepted_appoinment(request):
    if 'did' in request.session:
        seld=Appoinment.objects.filter(status=1,slot_id__doctor_id=request.session['did'])
        return render(request,'Doctor/View_Accept_Appoinment.html',{'seld':seld})
    else:
        return redirect('guest:Login')


def checkupdetails(request,cid):
    testty=TestType.objects.all()
    appid=Appoinment.objects.get(id=cid)
    if request.method=="POST":
        appid=Appoinment.objects.get(id=cid)
        testid=request.POST.get('test_details')
        ttid=Testdetails.objects.get(id=testid)
        Checkupdetails.objects.create(test_id=ttid,appoinment_id=appid,checkup_details=request.POST.get('details'))
        return render(request,'Doctor/Checkup_Details.html',{'TT':testty})
    else:
        return render(request,'Doctor/Checkup_Details.html',{'TT':testty})

def ajaxcheckup(request):
    testtype=request.GET.get('testd')
    tst=Testdetails.objects.filter(testtype=testtype)
    return render(request,"Doctor/Ajaxtest.html",{'tst':tst})

def view_checkup(request,vid):
    sel=Checkupdetails.objects.filter(appoinment_id=vid,checkup_status=1)
    return render(request,'Doctor/View_checkup.html',{'sel':sel})

def search_history(request):
    
    if request.method=="POST":
        uname=request.POST.get('u_name')
        user=UserRegistration.objects.get(name=uname)
        name=Checkupdetails.objects.filter(appoinment_id__User_id=user).count()
        
        if name>0:
            c=Checkupdetails.objects.filter(appoinment_id__User_id=user)
            # pd=Prescription.objects.filter(appoinment_id__User_id=user)
            app=Appoinment.objects.filter(User_id=user)
            res=Prescription.objects.filter(appoinment_id__in=app)
            return render(request,'Doctor/Search_History.html',{'sel':c,'pd':res})
        else:
            pr=Prescription.objects.filter(appoinment_id__User_id=user)
            return render(request,'Doctor/Search_History.html',{'pr':pr})
    else:
        return render(request,'Doctor/Search_History.html')

'''def gethistory(request):
    name=request.GET.get('uname')
    user=UserRegistration.objects.get(name=name)
    u=Checkupdetails.objects.filter(appoinment_id__User_id__name=user)
    return render(request,'Doctor/GetHistory.html',{'sel':u})'''


def prescription(request,pid):
    appid=Appoinment.objects.get(id=pid)
    if request.method=="POST":
        
        Prescription.objects.create(prescription_medicine=request.POST.get('prescription'),appoinment_id=appid)
        return render(request,'Doctor/Prescription.html')
    else:    
        return render(request,'Doctor/Prescription.html')

def complaintdoc(request):
    if request.method=="POST":
        doc=DoctorReg.objects.get(id=request.session['did'])
        Complaint.objects.create(title=request.POST.get('title'),content=request.POST.get('content'),Doctor_id=doc)
        seld=Complaint.objects.filter(Doctor_id=request.session['did'])
        return render(request,'Doctor/Complaint_Doc.html',{'seld':seld})
    else:
        seld=Complaint.objects.filter(Doctor_id=request.session['did'])
        return render(request,'Doctor/Complaint_Doc.html',{'seld':seld})

def descriptiondoc(request):  
    if request.method=="POST":
        doc=DoctorReg.objects.get(id=request.session['did'])
        Feedback.objects.create(description=request.POST.get('description'),Doctor_id=doc)
        seld=Feedback.objects.filter(Doctor_id=request.session['did'])  
        return render(request,'Doctor/description_doc.html',{'seld':seld})
    else:
        seld=Feedback.objects.filter(Doctor_id=request.session['did'])
        return render(request,'Doctor/description_doc.html',{'seld':seld})

def checkprescription(request,pid):
    check=Checkupdetails.objects.get(id=pid)
    appid=check.appoinment_id
    if request.method=="POST":
        
        Prescription.objects.create(prescription_medicine=request.POST.get('prescription'),appoinment_id=appid)
        return render(request,'Doctor/Prescription.html')
    else:    
        return render(request,'Doctor/Prescription.html')
def reference(request,vid):
    request.session['aid']=vid
    seld=DoctorReg.objects.all()
    return render(request,'Doctor/Refer.html',{'seld':seld})
   
def viewrefer(request):
    doc=DoctorReg.objects.get(id=request.session['did'])
    sel=refer.objects.filter(doctor_id_id=doc)
    return render(request,"Doctor/ViewRefers.html",{'sel':sel})
def sendrefer(request,vid):
    doc=DoctorReg.objects.get(id=vid)
    app=Appoinment.objects.get(id=request.session['aid'])
    refer.objects.create(doctor_id=doc,appoinment_id=app)
    del request.session['aid']
    return redirect('doctor:Home_Doctor')

    
def logout(request):
    if 'did' in request.session:
        del request.session["did"]
        return redirect("guest:Login")
    else:
        return redirect("guest:Login")

