from django.db import models

from datetime import date
from django.utils import timezone

class teacher_detail(models.Model):
    teacher_id = models.AutoField
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)
    GaurdainsName = models.CharField(max_length=30)
    Occupation = models.CharField(max_length=30 ,default="Agricultural")
    MailingAddress = models.CharField(max_length=30,default="Kathmandu")
    image = models.ImageField(upload_to='images/profile/', blank=True, null=True, default='/images/avatar.jpg')
    Gender = models.CharField(max_length=20 ,default="Male")
    PhoneNumber = models.CharField(max_length=10,default="None")
    Services=models.CharField(max_length=30,default="None")
    gmailid=models.CharField(max_length=30,default="None")
    LastteachingInstitution = models.CharField(max_length=400 ,default="None")
    runningteachingInstitution = models.CharField(max_length=1000,default="None")
    laststudyinstitution=models.CharField(max_length=100, default="None")
    PercentageinlastGrade = models.CharField(max_length=2,default="0")
    HigherGrade =models.CharField(max_length=2, default="one")
    experience=models.CharField(max_length=2,default="none")

    def __str__(self):
     return self.FirstName





#class student_fee(models.Model):
 # sid = models.ForeignKey(student_detail, on_delete=models.SET_DEFAULT)
  #monthlyfee = models.IntegerField()
  #Admissionfee = models.IntegerField()
  #Transportationfee = models.IntegerField()
  #Hostelfee = models.IntegerField()
  #def __str__(self):
   #   return self.sid




