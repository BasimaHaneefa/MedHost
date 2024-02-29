from django.db import models

# Create your models here.

class District(models.Model):
    district=models.CharField(max_length=50)

    def __str__(self):
        return self.district
    
class Place(models.Model):
    place=models.CharField(max_length=50)
    district=models.ForeignKey(District,on_delete=models.CASCADE)

    def __str__(self):
        return self.place
    

class TestType(models.Model):
    testtype=models.CharField(max_length=50)

    def __str__(self):
        return self.testtype
    

class Department(models.Model):
    department=models.CharField(max_length=50)

    def __str__(self):
        return self.department

class DoctorReg(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    address=models.TextField(null=True)
    gender=models.CharField(max_length=50)
    photo=models.FileField(upload_to='doctorphotos/')
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    experience=models.CharField(max_length=500)
    doj=models.DateField(auto_now_add=True)
    doctor_isactive=models.IntegerField(default=False)
    password=models.CharField(unique=True,max_length=50)


class Laboratory(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    address=models.TextField(null=True)
    photo=models.FileField(upload_to='labphotos/')
    doj=models.DateField(auto_now_add=True)
    password=models.CharField(unique=True,max_length=50)

class AdminLogin(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(unique=True,max_length=50)

class Slots(models.Model):
    slot_no=models.CharField(max_length=100)
    slot_date=models.DateField()
    slot_status=models.IntegerField(default=False)
    doctor_id=models.ForeignKey(DoctorReg,on_delete=models.CASCADE)



    




    