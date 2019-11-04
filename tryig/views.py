from django.shortcuts import render, redirect
from tryig.forms import EmployeeAdd
from tryig.models import Employee
# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeeAdd(request.POST, request.FILES)

        if form.is_valid():
            try:
                form.save()
                print("Successfully Create New Student")
                return redirect('/tryig/add1/')
            except:
                pass
    else:
        form = EmployeeAdd()
        print("error happen in the form")

    return render(request,'tryig/home.html',{'form':form})
def show(request):
    employees = Employee.objects.all()
    return render(request,"tryig/edit.html",{'employees':employees})
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'tryig/show.html', {'employee':employee})
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeAdd(request.POST, request.FILES, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/edit")
    return render(request, 'edit.html', {'employee': employee})
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")