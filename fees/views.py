import json
from django.shortcuts import render, redirect

import datetime

from fees.models import classfees
from . import views
def classfee(request):
    if request.method == 'POST':
         print(request.POST)
         classname =request.POST['class']
         academicyear = request.POST['academicyear']
         fees = request.POST['fees']


         f = classfees()
         f.classname = classname
         f.fees = fees
         f.year = academicyear
         f.save()


    return  render(request, 'fees/classfees.html')

def feedetails(request):
    currentyear =datetime.datetime.now();
    x=currentyear.year


    yearfrommodel = classfees.objects.all().filter( year=x)

    return render(request,'fees/classfees.html',{"year":yearfrommodel})




#def classfees(request):
   # try:
       # print(request.POST)
       # classname = request.POST['class']
       # academicyear = request.POST['academicyear']
        #fees = request.POST['fees']

        #f = classfees()
       # f.classname = classname
       # f.year = academicyear
        #f.fees = fees

       # f.save()
        #print("Saved")
    #except Exception as e:
       # print("Error in saving {}".format(e))
    # just wanted to retrive data from recent year
    #now = datetime.datetime.now()
    #x = now.year
    #print(x)
    # yearfrommodel = classfees.object.year
    # feedisplay = classfees.object.get( x=yearfrommodel )

    #return render(request, 'fees/classfees.html')  # ,{"feedisplay":feedisplay})
