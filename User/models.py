from django.db import models
from Admin.models import *
from Guest.models import *
# Create your models here.

class Appoinment(models.Model):
    appoinment_date=models.DateField(auto_now="True")
    for_date=models.DateField()
    slot_id=models.ForeignKey(Slots,on_delete=models.CASCADE)
    User_id=models.ForeignKey(UserRegistration,on_delete=models.CASCADE)
    status=models.IntegerField(default=0)


class Complaint(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(null=True)
    date=models.DateField(auto_now=True)
    reply=models.TextField(null=True)
    c_status=models.IntegerField(default=0)
    User_id=models.ForeignKey(UserRegistration,on_delete=models.SET_NULL,null=True)
    Doctor_id=models.ForeignKey(DoctorReg,on_delete=models.SET_NULL,null=True)
    Laboratory_id=models.ForeignKey(Laboratory,on_delete=models.SET_NULL,null=True)

class Feedback(models.Model):
    description=models.TextField(null=True)
    date=models.DateField(auto_now=True)
    User_id=models.ForeignKey(UserRegistration,on_delete=models.SET_NULL,null=True)
    Doctor_id=models.ForeignKey(DoctorReg,on_delete=models.SET_NULL,null=True)
    Laboratory_id=models.ForeignKey(Laboratory,on_delete=models.SET_NULL,null=True)



