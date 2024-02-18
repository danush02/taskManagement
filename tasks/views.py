from django.shortcuts import render,redirect
from .models import tasks,edittask
from employee.models import employee

# Create your views here.
def addtask(request):
    if request.POST:
        employeename = request.POST["employee"]
        task = request.POST["task"]
        taskcompletion = request.POST["completion_date"]
        tasks(empname=employeename,
              todotask=task,
              taskcompletion=taskcompletion,
              status=1).save() 
        return redirect("viewtask")
    emplist = employee.objects.all()
    return render(request,"task/addtask.html",{"emplist":emplist})

def viewtask(request):
    if request.POST:
        modify = request.POST["updatetask"].split(",")[1]
        taskID = request.POST["updatetask"].split(",")[0]
        if modify =="done":
            tasks.objects.filter(taskID=taskID).update(status=0)
        elif modify=="edit":
            edittask(taskID=taskID).save()
            return redirect("edittask")
    taskslist = tasks.objects.all()
    return render(request,"task/viewtask.html",{"tasks":taskslist})

def edittsk(request):
    if request.POST:
        taskid = edittask.objects.values_list("taskID",flat=True).first()
        employeename = request.POST["employee"]
        task = request.POST["task"]
        taskcompletion = request.POST["completion_date"]
        tasks.objects.filter(taskID=taskid).update(
                empname=employeename,
                todotask=task,
                taskcompletion=taskcompletion,
                status=1)
        edittask.objects.all().delete()
        return redirect("viewtask")
    emplist = employee.objects.all()
    return render(request,"task/edittask.html",{"emplist":emplist})