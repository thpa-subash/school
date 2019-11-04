from django.contrib import messages
from django.http import JsonResponse, response, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.shortcuts import render
from students.forms import NewStudentForm
from students.forms import feepay
from students.forms import classfees
from students.models import feeadd
from students.models import std_detail
from students.models import studentfee
from teacher.models import teacher_detail
from django.db.models import Q


from . import views
import datetime


def add_student(request):
    if request.method == "POST":
        form = NewStudentForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                form.save()

                return redirect('/students/approve/')
            except Exception as e:
                print(form)
                print("error suash occur ")
                print("Error in saving {}".format(e))
    else:
        form = NewStudentForm()
    return render(request,'students/new-student.html',{'form':form})




def newstd(request):
 return render(request, 'students/new-student.html')

def search(request):
    if request.method == 'POST':
        query = request.POST['q']

        if query :
            lookups = Q(FirstName__icontains=query) | Q(currentgrade__icontains=query)

            results = std_detail.objects.filter(lookups)
            print(results)
            if results:
                return render(request,'students/search.html',{'se':results})
            else:
                messages.error(request,'Result  not found')
        else:
            return HttpResponseRedirect("/students/search/")

    return render(request, 'students/search.html')

def studetsearchfees(request):
    if request.method == 'POST':
        query = request.POST['q']

        if query :
            lookups = Q(FirstName__icontains=query) | Q(currentgrade__icontains=query)

            results = std_detail.objects.filter(lookups)
            print(results)
            if results:
                return render(request,'students/studetsearchfees.html',{'se':results})
            else:
                messages.error(request,'Result  not found')
        else:
            return HttpResponseRedirect("/students/studetsearchfees/")

    return render(request, 'students/studetsearchfees.html')




def fees(request,id):
    now = datetime.datetime.now()

    newyear=now.year
    curentmonth =now.month
    day  = now.day
    print(day)
    studentdet = std_detail.objects.get(id=id)
    grade = studentdet.currentgrade
    fame = studentdet.FirstName
    id=studentdet.pk




    if grade:

        if studentdet.Hostel  == True:
            hostel = studentfee.objects.get(year = newyear,classnam=grade)
            hostel=hostel.hostelfee
            print(hostel)
        else:
            hostel=0

        if studentdet.Transportation  == True:
            trans = studentfee.objects.get(year=newyear, classnam=grade)
            transportatio = trans.transfee
        else:
            transportatio = 0


        if studentdet.Computer  == True:
            computer = studentfee.objects.get(year=newyear, classnam=grade)
            computerfee = computer.compfee
            print(computerfee)
        else:
            computerfee = 0

        if curentmonth == 1:
            admissionfe = studentfee.objects.get(year=newyear, classnam=grade)
            admission = admissionfe.admissionfee
            print(admission)

        else:
            admission = 0


        monthly = studentfee.objects.get(year=newyear,classnam=grade)
        monfee=monthly.monthlyfee

        if feeadd.objects.filter(studentname_id =id):
         feedet = feeadd.objects.filter(studentname_id =id).latest('paydate')
         dues=feedet.dues
         advace =feedet.advance
        else:
            dues = 0
            advace = 0





        totfee = hostel +  transportatio + computerfee + monfee+ admission+ dues - advace
        print(totfee)

        form = feepay()
        stdfee={'id':id,'fame':fame,'hos':hostel, 'transp':transportatio ,'com':computerfee ,'monthly':monfee,'admission':admission,'dues':dues,'advace':advace,'totfee':totfee}
        print(stdfee)





    return render(request,'students/fee.html',{'sd':stdfee,'form1':form})

def studentfeeupdate(request):
    if request.method == "POST":
        form = classfees(request.POST, request.FILES)

        if form.is_valid():
            try:

                form.save()

                print(form)
                return redirect('/students/feelist/')
            except Exception as e:
                print("error suash occur ")
                print("Error in saving {}".format(e))
    else:
        form = classfees()
    return render(request, 'fees/classfees.html', {'form': form})

#def feepay(request):
   # if request.method == "POST":
    #    form = feeclear(request.POST, request.FILES)

     #   if form.is_valid():
      #      try:

       #         form.save()

        #        print(form)
         #       return redirect('/students/studentfeeupdate/')
          #  except Exception as e:
           #     print("error suash occur ")
            #    print("Error in saving {}".format(e))
    #else:
     #   form = NewStudentForm()
    #return render(request, 'students/studetsearchfees.html', {'form': form})


def feelist(request):
    now = datetime.datetime.now()
    newyear = now.year
    print(newyear)

    feelist=studentfee.objects.filter(year = newyear)
    return render(request, 'fees/feelist.html',{'list':feelist})

def deletefeelist(request,id):
    feedelete = studentfee.objects.get(id=id)
    feedelete.delete()
    return render(request,'fees/feelist.html')




def student_details(request,id):
    data = std_detail.objects.get(id=id)
    return render(request, 'students/student_details.html',{'data':data})


def approve(request):
    teacher =teacher_detail.objects.all()

    students = std_detail.objects.all()
    print(students)
    print(teacher)


    return render(request, 'students/approve-student.html',{'students':students})

def edit_student(request,id):
    editstudent =std_detail.objects.get(id=id)
    return render(request,'students/edit-student.html',{'editstudent':editstudent})

def update_student(request,id):
    student = std_detail.objects.get(id=id)
    print(student)
    form = NewStudentForm(request.POST, request.FILES, instance = student)
    print(form)
    if form.is_valid():
        form.save()
        return redirect("/students/approve/")
    return render(request,'students/approve-students.html', {'students': student})


def update_fee(request,id):
   now = datetime.datetime.now()
   newyear = now.year
   curentmonth = now.month
   form = feepay(request.POST)
   studentdet = std_detail.objects.get(id=id)
   grade = studentdet.currentgrade
   fame = studentdet.FirstName
   if grade:

       if studentdet.Hostel == True:
           hostel = studentfee.objects.get(year=newyear, classnam=grade)
           hostel = hostel.hostelfee
           print(hostel)
       else:
           hostel = 0

       if studentdet.Transportation == True:
           trans = studentfee.objects.get(year=newyear, classnam=grade)
           transportatio = trans.transfee
       else:
           transportatio = 0

       if studentdet.Computer == True:
           computer = studentfee.objects.get(year=newyear, classnam=grade)
           computerfee = computer.compfee
           print(computerfee)
       else:
           computerfee = 0

       if curentmonth == 1:
           admissionfe = studentfee.objects.get(year=newyear, classnam=grade)
           admission = admissionfe.admissionfee
           print(admission)

       else:
           admission = 0

       monthly = studentfee.objects.get(year=newyear, classnam=grade)
       monfee = monthly.monthlyfee
       if feeadd.objects.filter(studentname_id=id):
         feedet = feeadd.objects.filter(studentname_id=id).latest('paydate')
         dues = feedet.dues
         advace = feedet.advance
       else:
           dues = 0
           advace = 0

       totfee = hostel + transportatio + computerfee + monfee + admission + dues - advace
       print(totfee)

   if form.is_valid():
       feeth = form.save(commit=False)
       if totfee>feeth.payment :
           dues= totfee - feeth.payment

       else:
           dues = 0

       if  totfee<feeth.payment :
           advance = feeth.payment - totfee
       else:
           advance = 0

       feeth.paydate=now
       feeth.dues=dues
       feeth.advance=advance
       feeth.studentname_id = id
       feeth.save()
   return redirect('/students/studentfees/')



def delete_student(request,id):
    studentdelete = std_detail.objects.get(id=id)
    studentdelete.delete()
    return render(request,'students/search.html')

