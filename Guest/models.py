from django.db import models
from Admin.models import Place

# Create your models here.
class UserRegistration(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    address=models.TextField(null=True)
    email=models.EmailField(unique=True)
    gender=models.CharField(max_length=50)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    photo=models.FileField(upload_to='userphotos/')
    proof=models.FileField(upload_to='userphotos/')
    password=models.CharField(unique=True,max_length=50)
    rg_date=models.DateField(auto_now_add=True)
    u_status=models.IntegerField(default=False)