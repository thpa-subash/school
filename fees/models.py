from django.db import models

class stdfee(models.Model):
    year = models.IntegerField()
    classname = models.CharField(max_length=1000)
    monthlyfee = models.IntegerField()
    admissionfee = models.IntegerField()
    transfee = models.IntegerField()
    compfee = models.IntegerField()
    hostelfee = models.IntegerField()

    def __str__(self):
        return self.classname
