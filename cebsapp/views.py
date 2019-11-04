from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Blog
from students.models import *
from teacher.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
    cout = std_detail.objects.count()

    coutteach = std_detail.objects.count()
    print(coutteach)
    # retrive 3 blog
    blogs = Blog.objects.all()[3:]
    return render(request, 'cebsapp/home.html', {'blogs': blogs,'cout':cout,'coutteach':coutteach})







def index(request):
    cout = std_detail.objects.count()
    print(cout)
    return render(request, 'cebsapp/index.html',{'cout':cout})



def edit(request):
    return render(request, 'cebsapp/edit-students.html')

def detailsstudent(request):
    return render(request, 'cebsapp/details-students.html')

# Create your views here.
#function for teacher
def teacherdetails(request):
    return render(request, 'cebsapp/teacher-details.html')

def editteacher(request):
    return render(request, 'cebsapp/edit-teacher.html')

def addteacher(request):
    return render(request, 'cebsapp/add-teacher.html')

#function for mail
def compose(request):
    return render(request,'cebsapp/inbox.html')
def inbox(request):
    return render(request,'cebsapp/viewmail.html')