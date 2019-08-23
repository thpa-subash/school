from .models import stdfee
from django .shortcuts import render


def classfee(request):
    if request.method == 'POST':
        print(request.POST)
        classname = request.POST['classname']
        year = request.POST['academicyear']
        afee = request.POST['afees']
        monthlyfee =request.POST['mfees']
        transfee =request.POST['transfees']
        compfee =request.POST['compfees']
        hostel =request.POST['hostel']



        cf=stdfee()
        cf.classname =classname
        cf.year = year
        cf.admissionfee =afee
        cf.monthlyfee =monthlyfee
        cf.transfee =transfee
        cf.compfee =compfee
        cf.hostelfee =hostel
        cf.save()


    return render (request,'fees/classfees.html')