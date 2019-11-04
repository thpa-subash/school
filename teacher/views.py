import json

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render

from teacher.models import teacher_detail
from teacher.forms import EmployeeAdd
from . import views
from django.db.models import Q
import datetime

# Create your views here.
"""def alldata():
    std = student_detail.objects.all()
    context = {'std': std}
    return context
"""


def add_teacher(request):
    if request.method == "POST":
        form = EmployeeAdd(request.POST, request.FILES)
        print(form)

        if form.is_valid():
            try:
                form.save()
                print("Successfully Create New Student")
                return redirect('/teacher/approve/')
            except Exception as e:
                print("error suash occur ")
                messages.error(request, 'Result  not found')
                print("Error in saving {}".format(e))
    else:
        form = EmployeeAdd()
        print("error happen in the form")
    return render(request, 'teacher/new-teacher.html', {'form': form})


def teacher_details(request):
    # data = student_detail.objects.all()
    return render(request, 'students/student_details.html')

def search(request):
    if request.method == 'POST':
        query = request.POST['q']

        if query :
            lookups = Q(FirstName__icontains=query)
            results = teacher_detail.objects.filter(lookups)
            print(results)
            if results:
                return render(request,'teacher/search.html',{'se':results})
            else:
                messages.error(request,'Result  not found')
        else:
            return HttpResponseRedirect("/teacher/search/")

    return render(request, 'teacher/search.html')
def approve(request):
    teacher = teacher_detail.objects.all()
    return render(request, 'teacher/approve-teacher.html', {'teacher': teacher})


def edit_teacher(request, id):
    editteacher = teacher_detail.objects.get(id=id)
    return render(request, 'teacher/edit-teacher.html', {'editteacher': editteacher})


def update(request, id):
    employee = teacher_detail.objects.get(id=id)
    form = EmployeeAdd(request.POST, request.FILES, instance=employee)
    print(form)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'teacher/approve-teacher.html', {'employee': employee})


def delete(request,id):
    teacherdelete = teacher_detail.objects.get(id=id)
    teacherdelete.delete()
    return redirect("/teacher/approve")
