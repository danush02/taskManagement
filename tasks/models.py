from django.db import models
import uuid
import datetime

# Create your models here.
class tasks(models.Model):
    taskID = models.UUIDField(auto_created=True, blank=False, default=uuid.uuid4)
    empname = models.TextField(blank=False)
    todotask = models.TextField(max_length=5000,blank=False)
    status = models.IntegerField(blank=False) #0-completed 1-Active
    taskcreation = models.DateTimeField(auto_now=True)
    taskcompletion = models.DateField(blank=False)

class edittask(models.Model):
    taskID = models.TextField(blank=False)