from django import forms
from .models import *

GEDER=[('Male','Male'),
       ('Female','Female'),]



class EmployeeAdd(forms.ModelForm):

    FirstName = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),required=True)
    LastName= forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),required=False)
    date = forms.DateField( widget=forms.DateInput(attrs={'class':'form-control','type':'date'}),required=False)

    GaurdainsName = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':' GaurdainsName','required':'False'}),required=False)
    gmailid =  forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':' Email id ','required':'False'}),required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'onchange':'document.getElementById("prepend-big-btn").value = this.value;','class':'form-control','type':'file', 'name':'image'}),required=False,)
    Occupation = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Occupation'}),required=False)
    MailingAddress = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Gaurdain Gmail Id',}),required=False)
    currentgrade = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'CurrentGrade'}),required=False)
    Gender = forms.ChoiceField(choices=GEDER,initial=0,widget=forms.RadioSelect(),required=False)
    PhoneNumber = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'PhoneNumber'}),required=False)
    FAVORITE_SERVICE = forms.ModelMultipleChoiceField(queryset=Services.objects.all(), required=False,
                                                      widget=forms.CheckboxSelectMultiple)

    LastteachingInstitution = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':' LastteachingInstitution'}),required=False)
    laststudyinstitution = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'laststudyinstitution'}),required=False)
    PercentageinlastGrade = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'PercentageinlastGrade'}),required=False)
    HigherGrade = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'HigherGrade'}),required=False)
    runningteachingInstitution =forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':'runningteachingInstitution'}),required=False)
    experience = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control','placeholder':' experience'}),required=False)


    class Meta():
        model = teacher_detail
        fields = ['FirstName','LastName','date','GaurdainsName','gmailid','image','Occupation','MailingAddress','currentgrade','Gender','PhoneNumber','FAVORITE_SERVICE','LastteachingInstitution','laststudyinstitution','PercentageinlastGrade','HigherGrade','runningteachingInstitution','experience' ]







