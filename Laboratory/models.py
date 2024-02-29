from django.db import models
from Admin.models import *

# Create your models here.

class Testdetails(models.Model):
    testtype=models.ForeignKey(TestType,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    test_amount=models.CharField(max_length=500)
    test_details=models.TextField(null=True)
    laboratory=models.ForeignKey(Laboratory,on_delete=models.CASCADE)