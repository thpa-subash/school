from django.shortcuts import render


def home(request):
    return render(request, 'cebsapp/home.html')


def index(request):
    return render(request, 'cebsapp/index.html')



def edit(request):
    return render(request, 'cebsapp/edit-student.html')

def detailsstudent(request):
    return render(request, 'cebsapp/details-student.html')

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