from django.shortcuts import render
from tasks.models import tasks

# Create your views here.
def homepage(request):
    inprogresslist = tasks.objects.filter(status=1).values_list("taskID",flat=True)
    completedlist = tasks.objects.filter(status=0).values_list("taskID",flat=True)

    return render(request,"homepage\index.html",{"inprogress":len(inprogresslist),"completed":len(completedlist)})