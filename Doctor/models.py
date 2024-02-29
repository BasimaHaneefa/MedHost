from django.db import models
from Laboratory.models import *
from User.models import *
# Create your models here.

class Checkupdetails(models.Model):
    appoinment_id=models.ForeignKey(Appoinment,on_delete=models.CASCADE)
    test_id=models.ForeignKey(Testdetails,on_delete=models.CASCADE)
    checkup_details=models.TextField(null=True)
    checkup_result=models.FileField(upload_to='checkupresult/',default=0)
    checkup_status=models.IntegerField(default=0)
class Prescription(models.Model):
    appoinment_id=models.ForeignKey(Appoinment,on_delete=models.CASCADE)
    prescription_medicine=models.TextField(null=True)
    prescription_date=models.DateField(auto_now=True)
    payment_status=models.IntegerField(default=0)

class refer(models.Model):
    appoinment_id=models.ForeignKey(Appoinment,on_delete=models.CASCADE)
    doctor_id=models.ForeignKey(DoctorReg,on_delete=models.CASCADE)
    

