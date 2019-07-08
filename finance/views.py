from django.shortcuts import render

def student(request):
     return render(request,'finance/student-search.html')

def resultstudent(request):
     return render(request,'finance/resultstudent.html')
def editfees(request):
     return render(request,'finance/editfeespayment.html')

def teacher(request):
     return render(request,'templates/student-search.html')

# Create your views here.
