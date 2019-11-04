from django import forms
from .models import *
OPTIONS =[
    ('oe', 'Are you a Regional OR National Player'),
    ('Football', 'Football'),
    ('Cricket', 'Cricket'),
    ('Basketball', 'Basketball'),
    ('Chess', 'Chess'),
    ('Badmintion', 'Badmintion'),
    ('Boxing', 'Boxing'),
    ('Running', 'Running'),

]
GEDER=[('male','Male'),
       ('female','Female'),]

FAVORITE_SERVICE = [
    ('Hostel', 'Hostel'),
    ('Transportation', 'Transportation'),
    ('Computer', 'Computer'),
]
"""class EmployeeAdd(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

"""
class EmployeeAdd(forms.ModelForm):

    FirstName = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),required=True)
    LastName= forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),required=False)
    date = forms.DateField( widget=forms.DateInput(attrs={'class':'form-control','type':'date'}),required=False)
    GaurdainsName = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':' GaurdainsName','required':'False'}),required=False)
    emailid =  forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':' Email id ','required':'False'}),required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'onchange':'document.getElementById("prepend-big-btn").value = this.value;','class':'form-control','type':'file', 'name':'image'}),required=False,)
    Occupation = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Occupation'}),required=False)
    MailingAddress = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Gaurdain Gmail Id',}),required=False)
    currentgrade = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'CurrentGrade'}),required=False)
    Gender = forms.ChoiceField(choices=GEDER,initial=0,widget=forms.RadioSelect(),required=False)
    PhoneNumber = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'PhoneNumber'}),required=False)
    FAVORITE_SERVICE= forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_SERVICE,
    )

    LastInstitution = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'LastInstitution'}),required=False)
    Percentage =forms.IntegerField( widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Percentage'}),required=False)
    Grade = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Grade'}),required=False)
    Players = forms.CharField(max_length=30,required=False)

    class Meta():
        model = Employee
        fields = ['FirstName','LastName','date','GaurdainsName','emailid','image','Occupation','MailingAddress','currentgrade','Gender','Players' ]







