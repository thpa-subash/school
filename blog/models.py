from django.db import models
from tinymce import HTMLField

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def tit(self):
        return self.title[:25]

    def summary(self):
        return self.body[:150]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title