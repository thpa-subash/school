import json
from django.shortcuts import render,redirect
from django.shortcuts import render
from student.forms import NewStudentForm
from student.models import student_detail
from student.models import studentfee

from . import views
import datetime






def add_student(request):
    try:
        print(request.POST)
        print(request.FILES)
        fname = request.POST['FirstName']
        lname = request.POST['lastname']
        date=request.POST['date']
        currentgrade=request.POST['cgrade']
        gaurdainname=request.POST['gname']
        maddress =request.POST['maddress']
        gender = request.POST['gender']
        players = request.POST['players']
        pnumber = request.POST['pnumber']
        student_photo =request.FILES.get('image',default='images/avatar.jpg')
        occupation=request.POST['occupation']
        service = request.POST.getlist('service[]')
        services = ' ,'.join(service)
        #service = request.POST['service']
        #print(request.service)
        #hobbies = request.POST['hobbies']
        institution = request.POST['linstitution']
        percentage = request.POST['percent']
        grade = request.POST['grade']
        gmailid = request.POST['emailid']

        s = student_detail()
        s.FirstName = fname
        s.LastName = lname
        s.date = date
        s.currentgrade=currentgrade
        s.Occupation=occupation
        s.gmailid = gmailid
        s.GaurdainsName=gaurdainname
        s.MailingAddress=maddress
        s.Gender=gender
        s.image = student_photo
        s.Players=players
        s.Services=service
        s.LastInstitution=institution
        s.Percentage=percentage
        s.PhoneNumber=pnumber
        s.date=date
        #s.Hobbies=str(hobbies)
        s.save()


        print("Successfully Create New Student")
    except Exception as e:
        print("Error in saving {}".format(e))
    return render(request, 'student/new-student.html')



def newstd(request):
 return render(request, 'student/new-student.html')


def fees(request,id):
    now = datetime.datetime.now()
    newyear=now.year
    curentmonth =now.month
    hostel =0
    transportatio =0
    computerfee = 0
    due =0
    advance = 0
    stdfee={}
    


    studentfees = student_detail.objects.get(id=id)
    grade = studentfees.currentgrade
    print(grade)

    if grade:

        if 'Hostel' in studentfees.Services:
            hostelf = studentfee.objects.get(year = newyear,classname=grade)
            hostel=hostelf.hostelfee

        if 'Transportation' in studentfees.Services:
            trans = studentfee.objects.get(year=newyear, classname=grade)
            transportatio = trans.transfee

        if 'Computer' in studentfees.Services:
            computer = studentfee.objects.get(year=newyear, classname=grade)
            computerfee = computer.compfee
            print(computerfee)
            
        if curentmonth == 1:
            admissionfe = studentfee.objects.get(year=newyear, classname=grade)
            admission = admissionfe.admissionfee
            print(admission)

        else:
            admission = 0







        monthly = studentfee.objects.get(year=newyear,classname=grade)
        monfee=monthly.monthlyfee

        stdfee={'hos':hostel, 'transp':transportatio ,'com':computerfee ,'monthly':monfee,'admission':admission}
        print(stdfee)


    return render(request,'student/fee.html',{'sd':stdfee})






def student_details(request):
    #data = student_detail.objects.all()
    return render(request, 'student/student_details.html')


def approve(request):
    students = student_detail.objects.all()
    return render(request, 'student/approve-student.html',{'students':students})

def edit_student(request,id):
    editstudent =student_detail.objects.get(id=id)
    return render(request,'student/edit-student.html',{'editstudent':editstudent})

def update(request,id):
    student = student_detail.objects.get(id=id)
    subash =student_detail(request.POST,instance = student)
    if subash.is_valid():
        subash.save()
        return redirect("/approve")
    return render(request,'student/edit-student.html',{'student':student})


def delete_student(request,id):
    studentdelete = student_detail.objects.get(id=id)

    studentdelete.delete()
    return redirect("/student/approve")

