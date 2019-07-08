from django.db import models
from datetime import date
from django.utils import timezone

#for inbox
class inbox(models.Model):
    email_id=models.EmailField()
    categories=models.CharField(max_length=100)
    subject=models.CharField(max_length=200)
    description=models.TextField()
    datetime = models.DateTimeField(default=timezone.now)
    save=models.IntegerField(max_length=1)
    discard=models.IntegerField(max_length=1)
    send=models.IntegerField(max_length=1)
    def __str__(self):
        return self.subject

#for blog and article
class blog(models.Model):
    title=models.CharField(max_length=400)
    date = models.DateField(auto_now=True)
    categories=models.CharField(max_length=100)
    description=models.TextField()
    #image
    author=models.CharField(max_length=200)
    status=models.CharField(max_length=1)
    def __str__(self):
        return self.title


