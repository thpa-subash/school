from django.db import models



class classfees(models.Model):


   classname = models.CharField(max_length=2)
   fees = models.CharField(max_length=10)
   year= models.CharField(max_length=10)
   def __str__(self):
     return self.classname






