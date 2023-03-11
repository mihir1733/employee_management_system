from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.

def employee_list(request):
    emps = Employee.objects.all()
    context = {
        'employee_list':emps
    }
    return render(request,'employee_register/employee_list.html',context)


def employee_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            emps = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            emps = EmployeeForm(instance=employee)
        return render(request,'employee_register/employee_form.html',{'emps':emps})
    else:
        if id == 0:
            emps = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            emps = EmployeeForm(request.POST,instance=employee)
        if emps.is_valid():
            emps.save()
        return redirect('/employee/list')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')