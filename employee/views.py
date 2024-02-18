from django.shortcuts import render,redirect
from .models import employee
# Create your views here.
def addemp(request):
    if request.POST:
        empname = request.POST["employee_name"]
        empmail = request.POST["employee_email"]
        gender = request.POST["gender"]
        role = request.POST["role"]
        employee(empname=empname,
                 empemail=empmail,
                 emprole=role,
                 empgender=gender).save()
        return redirect("homepage")
    return render(request,"employee/addemployee.html")