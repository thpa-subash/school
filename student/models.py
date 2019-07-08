from django.db import models

from datetime import date
from django.utils import timezone

class student_detail(models.Model):
    student_id = models.AutoField
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)
    GaurdainsName = models.CharField(max_length=30)
    Occupation = models.CharField(max_length=30)
    MailingAddress = models.CharField(max_length=30)

    Gender = models.CharField(max_length=20)
    PhoneNumber = models.CharField(max_length=10)
    Hobbies = models.CharField(max_length=20)
    Transportaion = models.IntegerField()
    Hostel = models.IntegerField()
    LastInstitution = models.CharField(max_length=40)
    Percentage = models.CharField(max_length=2)
    Grade =models.CharField(max_length=2)
    Players = models.CharField(max_length=30)
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




