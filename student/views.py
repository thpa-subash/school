import json

from django.shortcuts import render

from student.forms import NewStudentForm
from student.models import student_detail
from . import views

# Create your views here.
"""def alldata():
    std = student_detail.objects.all()
    context = {'std': std}
    return context
"""


def newstd(request):
    """if request.method == 'POST':
        std = student_detail(
        FirstName=request.POST['FirstName'],
        LastName=request.POST['lastname'],
        date=request.POST['date'],
        GaurdainsName=request.POST['gname'],
        Occupation=request.POST['occupation'],
        MailingAddress=request.POST['maddress'],
        Gender=request.POST['gender'],
        PhoneNumber=request.POST['pnumber'],
        Hobbies=request.POST['hobbies'],
        Transportaion=request.POST['trans'],
        Hostel=request.POST['hostel'],
        LastInstitution=request.POST['linstitution'],
        Percentage=request.POST['percent'],
        Grade=request.POST['grade'],
        Players=request.POST['players']
    ),"""

    return render(request, 'student/new-student.html')




def add_student(request):
    # if request.method == 'POST':
    #     # body_unicode = request.body.decode('utf-8')
    #     print(request.body['FirstName'])
    #     print(request.body['LastName'])
        # body = json.loads(body_unicode)
        # s= student_detail()
        # print(body['FirstName'])
        # s.FirstName = body['FirstName']
        # s.save()
        # print("S is saved "   + s)
    try:
        fname = request.POST['FirstName']
        lname = request.POST['FirstName']
        s = student_detail()
        s.FirstName = fname
        s.LastName = lname
        s.Transportaion = 1
        s.Hostel = 1
        s.save()
        print("Saved")
    except Exception as e:
        print("Error in saving {}".format(e))
    return render(request, 'student/new-student.html')


def approve(request):
    return render(request, 'student/approve-student.html')


def delete(request):
    return render(request, 'student/delete-student.html')


def example(request):
    FirstName = "not logged in"
    if request.method == "POST":
        # Get the posted form
        MyLoginForm = newstudent(request.POST)

        if MyLoginForm.is_valid():
            FirstName = MyLoginForm.cleaned_data['FirstName']
        newstudent.save()
        print("student form saved")

    return render(request, 'student/eg.html', {"FirstName": FirstName})
