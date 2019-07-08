"""cebs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include

import cebsapp
from cebsapp import views
from django.conf import settings
from django.conf.urls.static import static

import student
from student import views
import finance
from finance import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cebsapp.views.home, name="home"),
    #student urls
    path('student/',include('student.urls')),
   # path('newstudent/', student.views.new, name="New Student"),

    path('index/',cebsapp.views.index , name="index"),
    path('home/' ,cebsapp.views.home ,name="home"),

    path('edit-student/', cebsapp.views.edit ,name="edit"),
    path('details-student/', cebsapp.views.detailsstudent , name="details"),
    #teacher urls
    path('addteacher/', cebsapp.views.addteacher ,name="tadd"),
    path('editteacher/', cebsapp.views.editteacher ,name="tedit"),
    path('teacherdetails/', cebsapp.views.teacherdetails,name="tdetails"),
    #mail urls
    path('mailbox/',include('cebsapp.urls')),
    #path('mailcompose/', cebsapp.views.compose,name="compose"),
    #//path('inbox/', cebsapp.views.inbox,name="tdetails"),
    #finance urls
    path('studentfees/',finance.views.student, name="Student Fees"),
    path('resultstudent/',finance.views.resultstudent, name="Student Result"),
    path('editfeespayment/',finance.views.editfees, name="Student Result"),
    path('teacherpayment/',finance.views.teacher, name="Teacher Payment"),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
