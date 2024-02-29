from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from .models import *
from Doctor.models import *
# Create your views here.
def district(request):
    seld=District.objects.all()
    if request.method=="POST":
        District.objects.create(district=request.POST.get('district'))
        seld=District.objects.all()
        return render(request,'Admin/district.html',{'dis':seld})
    return render(request,'Admin/district.html',{'dis':seld})

def dltdis(request,did):
    District.objects.get(id=did).delete() 
    return redirect('webadmin:district')

def updis(request,uid):
    seldis=District.objects.get(id=uid)
    if request.method=="POST":
        seldis.district=request.POST.get('district')
        seldis.save()
        return redirect('webadmin:district')
    else:
        return render(request,'Admin/EditDis.html',{'Edis':seldis})

def place(request):
    disob=District.objects.all()
    selp=Place.objects.all()
    if request.method=="POST":
        disid=request.POST.get('district')
        dis=District.objects.get(id=disid)
        Place.objects.create(place=request.POST.get('place'),district=dis)
        selp=Place.objects.all()
        return render(request,'Admin/place.html',{'Dis':disob,'Plc':selp})
    else:
        return render(request,'Admin/place.html',{'Dis':disob,'Plc':selp})

def dltplace(request,did):
    Place.objects.get(id=did).delete()
    return redirect('webadmin:place')


def upplace(request,uid):
    disob=District.objects.all()
    selplc=Place.objects.get(id=uid)
    if request.method=="POST":
        disid=request.POST.get('district')
        selplc.district=District.objects.get(id=disid)
        selplc.place=request.POST.get('place')
        selplc.save()
        return redirect('webadmin:place')
    else:
        return render(request,"Admin/EditPlace.html",{'Dis':disob,'selp':selplc})


def testtype(request):
    seld=TestType.objects.all()
    if request.method=="POST":
        TestType.objects.create(testtype=request.POST.get('testtype'))
        seld=TestType.objects.all()
        return render(request,'Admin/testtype.html',{'tst':seld})
    return render(request,'Admin/testtype.html',{'tst':seld})

def dlttst(request,did):
    TestType.objects.get(id=did).delete()
    return redirect('webadmin:testtype')

def uptest(request,uid):
    seld=TestType.objects.get(id=uid)
    if request.method=="POST":
        seld.testtype=request.POST.get('testtype')
        seld.save()
        return redirect('webadmin:testtype')
    else:
        return render(request,'Admin/EditTest.html',{'Etst':seld})

def department(request):
    seld=Department.objects.all()
    if request.method=="POST":
        Department.objects.create(department=request.POST.get('department'))
        seld=Department.objects.all()
        return render(request,'Admin/department.html',{'dep':seld})
    return render(request,'Admin/department.html',{'dep':seld})

def dltdep(request,did):
    Department.objects.get(id=did).delete()
    return redirect('webadmin:department')

def updep(request,uid):
    seld=Department.objects.get(id=uid)
    if request.method=="POST":
        seld.department=request.POST.get('department')
        seld.save()
        return redirect('webadmin:department')
    else:
        return render(request,'Admin/EditDept.html',{'Edep':seld})

def newdoctor(request):
    seld=Department.objects.all()
    if request.method=="POST" and request.FILES:

        disid=request.POST.get('department')
        dis=Department.objects.get(id=disid)

        DoctorReg.objects.create(name=request.POST.get('name'),contact=request.POST.get('contact'),
        email=request.POST.get('email'),address=request.POST.get('address'),
        gender=request.POST.get('gender'),photo=request.FILES.get('image'),
        department=dis,experience=request.POST.get('experience'),password=request.POST.get('password'))

        selp=DoctorReg.objects.all()
        return render(request,'Admin/NewDoctor.html',{'dep':seld,'doc':selp})
    else:
        selp=DoctorReg.objects.all()
        return render(request,'Admin/NewDoctor.html',{'dep':seld,'doc':selp})

def dltdoctor(request,did):
    DoctorReg.objects.get(id=did).delete()
    return redirect('webadmin:newdoctor')
        
def newlab(request):
    
    if request.method=="POST" and request.FILES:
        Laboratory.objects.create(name=request.POST.get('name'),contact=request.POST.get('contact'),
        email=request.POST.get('email'),address=request.POST.get('address'),
        photo=request.FILES.get('image'),password=request.POST.get('password'))
        sellab=Laboratory.objects.all()
        return render(request,'Admin/NewLab.html',{'lab':sellab})
    else:
        sellab=Laboratory.objects.all()
        return render(request,'Admin/NewLab.html',{'lab':sellab})

def dltlab(request,did):
    Laboratory.objects.get(id=did).delete()
    return redirect('webadmin:newlab')


def viewuser(request):
    seld=UserRegistration.objects.filter(u_status=0)
    return render(request,'Admin/ViewUser.html',{'seld':seld})

def acceptuser(request,aid):
    selu=UserRegistration.objects.get(id=aid)
    name=selu.name
    email1=selu.email
    send_mail(
            'Respected sir/madam '+name, #subject
            "\rVerification Successfully Complted Thanks to Join Us.",#body
            settings.EMAIL_HOST_USER,
            [email1],

        )
    selu.u_status=True 
    selu.save()
    return redirect('webadmin:viewuser')

def rejectuser(request,rid):
    selu=UserRegistration.objects.get(id=rid)
    name=selu.name
    email1=selu.email
    send_mail(
            'Respected sir/madam '+name, #subject
            "\rVerification Rejected  PLEASE Check Your Details....",#body
            settings.EMAIL_HOST_USER,
            [email1],

        )
    selu.u_status=2 
    selu.save()
    return redirect('webadmin:viewuser')

def accepteduser(request):
    seld=UserRegistration.objects.filter(u_status=1)
    return render(request,'Admin/AcceptList.html',{'seld':seld})

def rejecteduser(request):
    seld=UserRegistration.objects.filter(u_status=2)
    return render(request,'Admin/RejectList.html',{'seld':seld})

def home(request):
    doctorcount=DoctorReg.objects.all().count()
    labcount=Laboratory.objects.all().count()
    patientcount=UserRegistration.objects.all().count()
    doctor=DoctorReg.objects.all()
    lab=Laboratory.objects.all()
    return render(request,'Admin/Home.html',{"dcount":doctorcount,"lcount":labcount,"pcount":patientcount,"dr":doctor,"lab":lab})

def viewappoinment(request):
    seld=Appoinment.objects.filter(status=0)
    return render(request,'Admin/Appoinment_View.html',{'seld':seld})
    
def acceptappoinment(request,app):
    selu=Appoinment.objects.get(id=app)
    name=selu.User_id.name
    email1=selu.User_id.email
    send_mail(
            'Respected sir/madam '+name, #subject
            "\rYour Appointment is Accepted.",#body
            settings.EMAIL_HOST_USER,
            [email1],

        )
    selu.status=True 
    selu.save()
    return redirect('webadmin:viewappoinment')
    
def rejectappoinment(request,rpp):
    selu=Appoinment.objects.get(id=rpp)
    name=selu.User_id.name
    email1=selu.User_id.email
    send_mail(
            'Respected sir/madam '+name, #subject
            "\rYour Appointment Is Rejected.",#body
            settings.EMAIL_HOST_USER,
            [email1],

        )
    selu.status=2 
    selu.save()
    return redirect('webadmin:viewappoinment')

def viewcomplaint(request):
    seld=Complaint.objects.filter(Doctor_id_id__gt=0)
    lab=Complaint.objects.filter(Laboratory_id_id__gt=0)
    user=Complaint.objects.filter(User_id_id__gt=0) 
    return render(request,'Admin/View_Complaint.html',{'seld':seld,'lab':lab,'user':user})

def viewfeedback(request):
    seld=Feedback.objects.filter(Doctor_id_id__gt=0)
    lab=Feedback.objects.filter(Laboratory_id_id__gt=0)
    user=Feedback.objects.filter(User_id_id__gt=0) 
    return render(request,'Admin/View_Feedback.html',{'seld':seld,'lab':lab,'user':user})

def reply(request,did):
    seld=Complaint.objects.get(id=did)
    if request.method=="POST":
        seld.reply=request.POST.get('reply')
        seld.c_status=1
        seld.save()
        return redirect('webadmin:viewcomplaint')
    else:
        return render(request,'Admin/Reply.html',{'doc':seld})

def slots(request,dcid):
    doc=DoctorReg.objects.get(id=dcid)
    if request.method=="POST":
        count=int(request.POST.get('count'))
        da=request.POST.get('date')
        for i in range(1,count+1):
            Slots.objects.create(slot_no=i,slot_date=da,doctor_id=doc)
        return redirect('webadmin:newdoctor')
    return render(request,'Admin/Add_Slots.html')


def report(request):
    if request.method=="POST":
        datefrom=request.POST.get('from_date')
        todate=request.POST.get('to_date')
        sel=Appoinment.objects.filter(slot_id__slot_date__lt=todate,slot_id__slot_date__gt=datefrom)
        return render(request,'Admin/Report.html',{'sel':sel})
    return render(request,'Admin/Report.html')

def lbreport(request):
    if request.method=="POST":
        datefrom=request.POST.get('from_date')
        todate=request.POST.get('to_date')
        check=Checkupdetails.objects.filter(appoinment_id__slot_id__slot_date__lt=todate,appoinment_id__slot_id__slot_date__gt=datefrom)
        return render(request,'Admin/Lab_Report.html',{'sel':check})
    return render(request,'Admin/Lab_Report.html')


def logout(request):
    if 'aid' in request.session:
        del request.session["aid"]
        return redirect("webguest:Login")
    else:
        return redirect("webguest:Login")
