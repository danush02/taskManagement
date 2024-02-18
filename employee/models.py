from django.db import models
import uuid

# Create your models here.
class employee(models.Model):
    employeeID = models.UUIDField(auto_created=True, blank=False, default=uuid.uuid4)
    empname = models.TextField(max_length=500,blank=False)
    empemail = models.TextField(max_length=500,blank=False)
    emprole = models.TextField(max_length=500,blank=False,default="blank")
    empgender = models.TextField(max_length=10,blank=False)
    empcreation = models.DateTimeField(auto_now=True)