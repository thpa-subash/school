from django.db import models
from datetime import date,datetime
from django.utils import timezone



class std_detail(models.Model):
    student_id = models.AutoField
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=False,auto_now=False,blank=True)
    GaurdainsName = models.CharField(max_length=30)
    emailid =models.CharField(max_length=40,default="none")
    image = models.ImageField(upload_to='images/profile/', blank=True,null=True,default='/images/avatar.jpg')

    Occupation = models.CharField(max_length=30 ,default="Agricultural")
    MailingAddress = models.CharField(max_length=30,default="Kathmandu")
    classch = (('One', 'One'),
                   ('Two', 'Two'),
                   ('Three', 'Three'),
                   ('Four', 'Four'),
                   ('Five', 'Five'),
                   ('Six', 'Six'),
                   ('Seven', 'Seven'),
                   ('Eight', 'Eight'),
                   ('Nine', 'Nine'),
                   ('Ten', 'Ten'),

                   )
    currentgrade = models.CharField(max_length=30,default="Two", choices=classch)
    Gender = models.CharField(max_length=20 ,default="Male")
    PhoneNumber = models.CharField(max_length=10,default="None")
    Hobbies = models.CharField(max_length=20 ,default="none")

    dues=models.IntegerField(default="0")
    payment=models.IntegerField(default="0")

    Transportation = models.BooleanField(default=False)
    Hostel = models.BooleanField(default=False)
    Computer = models.BooleanField(default=False)
    LastInstitution = models.CharField(max_length=40 ,default="None")
    Percentage = models.CharField(max_length=2,default="0")
    Grade =models.CharField(max_length=2, default="one")
    Players = models.CharField(max_length=30,default="None")

    class Meta:
        db_table = "std_detail"

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




yearchoice = (('Select Year', 'Select Year'),
                ('2019', '2019'),
              ('2020', '2020'),
              ('2021', '2021'),
              ('2022', '2022'),
              ('2023', '2023'),
              ('2023', '2024'),)
classchoice = (('One', 'One'),
               ('Two', 'Two'),
               ('Three', 'Three'),
               ('Four', 'Four'),
               ('Five', 'Five'),
                ('Six', 'Six'),
                ('Seven', 'Seven'),
                ('Eight', 'Eight'),
                ('Nine', 'Nine'),
                ('Ten', 'Ten'),

               )


class studentfee(models.Model):
    year = models.CharField(max_length=1000, blank=True, null=True, choices=yearchoice)
    classnam = models.CharField(max_length=1000, blank=True, null=True, choices=classchoice)
    monthlyfee = models.IntegerField()
    admissionfee = models.IntegerField()
    transfee = models.IntegerField()
    compfee = models.IntegerField()
    hostelfee = models.IntegerField()


    def __str__(self):
        return self.classnam


class feeadd(models.Model):
    studentname = models.ForeignKey(std_detail, on_delete=models.CASCADE)
    payment = models.IntegerField(default=0)
    dues = models.IntegerField(default=0)
    advance = models.IntegerField(default=0)
    paydate = models.DateTimeField()


    def __str__(self):
     return self.studentname.FirstName

