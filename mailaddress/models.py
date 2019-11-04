from datetime import datetime

from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

class mailaddress(models.Model):

   to = models.CharField(max_length=20)
   subject = models.CharField(max_length=1000)
   body = RichTextField(blank=True,null=True)



   def __str__(self):
       return self.subject

