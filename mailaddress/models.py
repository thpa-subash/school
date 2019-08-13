from django.db import models

class mailaddress(models.Model):

   to = models.CharField(max_length=20)
   subject = models.CharField(max_length=1000)
   body = models.TextField()

   def __str__(self):
       return self.subject