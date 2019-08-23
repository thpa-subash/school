import json
from django.shortcuts import render, redirect
from django.shortcuts import render

from teacher.models import teacher_detail
from . import views

# Create your views here.
"""def alldata():
    std = student_detail.objects.all()
    context = {'std': std}
    return context
"""


def add_teacher(request):
    try:
        print(request.POST)
        fname = request.POST['FirstName']
        lname = request.POST['lastname']
        date = request.POST['date']
        gaurdainname = request.POST['gname']
        maddress = request.POST['maddress']
        teacher_photo = request.FILES.get('image', default='images/avatar.jpg')

        gender = request.POST['gender']
        lti = request.POST['LastteachingInstitution']
        rti = request.POST['runningteachingInstitution']
        lsi = request.POST['laststudyinstitution']
        pilg = request.POST['PercentageinlastGrade']
        gmailid=request.POST['gmailid']

        HigherGrade = request.POST['HigherGrade']
        experience=request.POST['experience']


        pnumber = request.POST['pnumber']
        occupation = request.POST['occupation']

        service = request.POST.getlist('service[]')
        services= ' ,'.join(service)

        # print(request.service)
        # hobbies = request.POST['hobbies']



        t = teacher_detail()
        t.FirstName = fname
        t.LastName = lname
        t.date = date
        t.Occupation = occupation
        t.GaurdainsName = gaurdainname
        t.MailingAddress = maddress
        t.image = teacher_photo
        t.Gender = gender
        t.Services=services
        t.gmailid=gmailid


        t.LastteachingInstitution = lti
        t.runningteachingInstitution = rti
        t.laststudyinstitution=lsi
        t.PercentageinlastGrade=pilg
        t.HigherGrade=HigherGrade
        t.experience=experience
        t.PhoneNumber = pnumber
        t.save()

        print("Saved")
    except Exception as e:
        print("Error in saving {}".format(e))
    return render(request, 'teacher/new-teacher.html')



def teacher_details(request):
    # data = student_detail.objects.all()
    return render(request, 'student/student_details.html')


def approve(request):
    teacher = teacher_detail.objects.all()
    return render(request, 'teacher/approve-teacher.html', {'teacher': teacher})


def edit_teacher(request, id):
    editteacher = teacher_detail.objects.get(id=id)
    return render(request, 'teacher/edit-teacher.html', {'editteacher': editteacher})


def update(request, id):
    student = teacher_detail.objects.get(id=id)
    subash = teacher_detail(request.POST, instance=student)
    if subash.is_valid():
        subash.save()
        return redirect("/approve")
    return render(request, 'student/edit-student.html', {'student': student})


def delete(request,id):
    teacherdelete = teacher_detail.objects.get(id=id)
    teacherdelete.delete()
    return redirect("/teacher/approve")
