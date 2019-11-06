from django.core.mail import send_mail
from django.http import JsonResponse
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

@staticmethod
def send_email(url, toaddr, body, subject):
            gmail_user = 'subashthapa901@gmail.com'
            gmail_password = 'PASSWORD'

            email_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            email_server.login(gmail_user, gmail_password)

            msg = MIMEMultipart()
            msg['From'] = gmail_user
            msg['To'] = toaddr
            msg['Subject'] = subject

            # body = "YOUR BODY GOES HERE"
            msg.attach(MIMEText(body, 'plain'))
            text = msg.as_string()
            email_server.sendmail(gmail_user, toaddr, text)
            email_server.close()
            send_mail(subject, body, settings.EMAIL_HOST_USER,recievers )

def inbox(request):
   inbox = mailaddress.objects.all()
   return render(request, 'mailaddress/inbox.html',{'inbox':inbox})




def getData(request):
    labels = ["sds","Sds"]
    data = [111,121]
    return JsonResponse({'labels': labels, 'data' : data})
