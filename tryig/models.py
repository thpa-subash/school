from django.db import models
from django.utils import timezone
class Employee(models.Model):
    student_id = models.AutoField
    FirstName = models.CharField(max_length=20,default="None")

    LastName = models.CharField(max_length=20,default="None")
    date = models.DateField(default=timezone.now)
    GaurdainsName = models.CharField(max_length=30,default="None")
    emailid = models.CharField(max_length=20, default="none")
    image = models.ImageField(upload_to='images/profile/', blank=True, null=True, default='/images/avatar.jpg')

    Occupation = models.CharField(max_length=30, default="Agricultural")
    MailingAddress = models.CharField(max_length=30, default="Kathmandu")
    currentgrade = models.CharField(max_length=30, default="none")

    Gender = models.CharField(max_length=20, default="Male")
    PhoneNumber = models.CharField(max_length=10, default="None")
    Hobbies = models.CharField(max_length=20, default="none")
    Services = models.CharField(max_length=30, default="None")
    LastInstitution = models.CharField(max_length=40, default="None")
    Percentage = models.CharField(max_length=2, default="0")
    Grade = models.CharField(max_length=2, default="o")
    Players = models.CharField(max_length=30, default="None")

    class Meta:
        db_table = "employee"

    def __str__(self):
     return self.FirstName