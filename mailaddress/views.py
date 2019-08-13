from django.core.mail import send_mail
#from django.http import HttpResponse
import json
from django .shortcuts import render,redirect
from mailaddress.models import mailaddress
#from student.models import student_detail
from . import views

def compose(request):
    try:
        print(request.POST)
        #cateo=request.POST['cateo']
        to = request.POST['to']
        subject = request.POST['subject']
        body = request.POST['body']
        #if request.POST['to']== 'student':
           # students = student_detail.objects.GaurdainsName()
          #  print(students)


        #send_mail(subject, body, 'gurkhasarmy@gmail.com', ['nepalisubashthapa@gmail.com',], fail_silently=False)
        #send_mail('subject', 'body', 'subashthapa901@gmail.com', ['nepalisubashthapa@gmail.com',], fail_silently=False)
        compose=mailaddress()
 
        compose.to=to
        compose.subject=subject
        compose.body=body
        compose.save()
        print("Saved")

    except Exception as e:
     print("Error in saving {}".format(e))
    return render(request, 'mailaddress/compose.html')

def inbox(request):
   inbox = mailaddress.objects.all()
   return render(request, 'mailaddress/inbox.html',{'inbox':inbox})




