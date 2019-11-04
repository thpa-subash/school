from django.core.mail import send_mail
#from django.http import HttpResponse
import json
from .forms import mailaddress1, settings
from django .shortcuts import render,redirect
from mailaddress.models import mailaddress
from students.models import std_detail
from . import views

def compose(request):
    if request.method == "POST":
        form = mailaddress1(request.POST, request.FILES)
        to = request.POST['to']

        subject = request.POST['subject']
        body = request.POST['body']

        recievers = []
        for email in std_detail.objects.all():
            recievers.append(email.emailid)





        send_mail(subject, body, settings.EMAIL_HOST_USER,recievers )


        return redirect('/mailaddress/inbox/')

    else:
        form = mailaddress1()
        print("error suash occur ")

    return render(request, 'mailaddress/compose.html', {'form': form})

def inbox(request):
   inbox = mailaddress.objects.all()
   return render(request, 'mailaddress/inbox.html',{'inbox':inbox})




