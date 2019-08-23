from django.db import models

from datetime import date
from django.utils import timezone


class student_detail(models.Model):
    student_id = models.AutoField
    FirstName = models.CharField(max_length=20)

    LastName = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)
    GaurdainsName = models.CharField(max_length=30)
    emailid =models.CharField(max_length=20,default="none")
    image = models.ImageField(upload_to='images/profile/', blank=True,null=True,default='/images/avatar.jpg')

    Occupation = models.CharField(max_length=30 ,default="Agricultural")
    MailingAddress = models.CharField(max_length=30,default="Kathmandu")

    Gender = models.CharField(max_length=20 ,default="Male")
    PhoneNumber = models.CharField(max_length=10,default="None")
    Hobbies = models.CharField(max_length=20 ,default="none")
    Services=models.CharField(max_length=30,default="None")
    LastInstitution = models.CharField(max_length=40 ,default="None")
    Percentage = models.CharField(max_length=2,default="0")
    Grade =models.CharField(max_length=2, default="one")
    Players = models.CharField(max_length=30,default="None")
    def __str__(self):
     return self.FirstName





#class fee(models.Model):
 #   studentname =models.ForeignKey(student_detail,on_delete=models.CASCADE)
#
 #   monthlyfees =models.ForeignKey(classfee,on_delete=models.CASCADE)
  #  due =models.IntegerField()
   # advance =models.IntegerField()

    #def __str__(self):

     #   return self.studentname.FirstName




#class student_fee(models.Model):
 # sid = models.ForeignKey(student_detail, on_delete=models.SET_DEFAULT)
  #monthlyfee = models.IntegerField()
  #Admissionfee = models.IntegerField()
  #Transportationfee = models.IntegerField()
  #Hostelfee = models.IntegerField()
  #def __str__(self):
   #   return self.sid




