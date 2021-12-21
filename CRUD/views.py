from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee

def home(request):
    emp = Employee.objects.order_by('id')
    context={
        'emp':emp
    } 
    return render (request , 'CRUD/home.html',context)


def add_emp(request):
    if request.method=='POST':
        form =EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form =EmployeeForm()
    return render (request , 'CRUD/add_emp.html',{'form':form})


def delete_emp(reques,id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect ('home')

def update_emp(request,id):
    emp = Employee.objects.get(id=id)
    form = EmployeeForm(instance=emp)
    if request.method=='POST':
        form = EmployeeForm(request.POST,instance=emp)
        if form.is_valid(): 
            
            form.save()
            return redirect('home')
    else:
        return render(request ,'CRUD/update_emp.html',{'form':form ,})
    