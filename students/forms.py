from django import forms
from .models import *
from django.utils import timezone

gender_choice = [('Male', 'Male'), ('Female', 'Female'),('Others','Others')]
players =[
    ('oe', 'Are you a Regional OR National Player'),
    ('Football', 'Football'),
    ('Cricket', 'Cricket'),
    ('Basketball', 'Basketball'),
    ('Chess', 'Chess'),
    ('Badmintion', 'Badmintion'),
    ('Boxing', 'Boxing'),
    ('Running', 'Running'),

]
classchoice = (('One', 'One'),
               ('Two', 'Two'),
               ('Three', 'Three'),
               ('Four', 'Four'),
               ('Five', 'Five'),
                ('Six', 'Six'),
                ('Seven', 'Seven'),
                ('Eight', 'Eight'),
                ('Nine', 'Nine'),
                ('Ten', 'Ten'),

               )



class NewStudentForm(forms.ModelForm):
    FirstName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                                )

    LastName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',}),
                               )
    date = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),)
    GaurdainsName = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' GaurdainsName', }),required=False
        )
    emailid = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Email id ', }),
        required=False)
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'onchange': 'document.getElementById("prepend-big-btn").value = this.value;', 'class': 'form-control',
               'type': 'file', 'name': 'image'}), required=False )
    Occupation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Occupation',}),required=False
                                 )
    MailingAddress = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gaurdain Gmail Id', }),required=False)
    currentgrade = forms.ChoiceField(choices=classchoice,initial='Select Grade',
        widget=forms.Select(attrs={'class': 'form-control', }),required=False)
    Gender = forms.ChoiceField(choices=gender_choice, initial=0, widget=forms.RadioSelect(),required=False)
    PhoneNumber = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PhoneNumber','required': 'False'}),
                                  )


    LastInstitution = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'LastInstitution'}), required=False)
    Percentage = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Percentage'}), required=False)
    Grade = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Grade'}),required=False
                            )
    Players = forms.CharField(max_length=30, required=False)

    class Meta():
        model = std_detail
        fields = ['FirstName', 'LastName', 'date', 'GaurdainsName', 'emailid', 'image', 'Occupation', 'MailingAddress',
                  'currentgrade', 'Gender','PhoneNumber','Hostel','Transportation','Computer', 'LastInstitution','Percentage','Grade','Players']




class classfees(forms.ModelForm):
   monthlyfee = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mothly fees'}),)
   admissionfee = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'admisio fees'}),)
   transfee = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'transfee'}),)
   compfee = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'compfee'}),)
   hostelfee = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'hostelfee'}),)
   class Meta():
       model = studentfee
       fields = ['year','classnam','monthlyfee', 'admissionfee', 'transfee','compfee','hostelfee' ]


class feepay(forms.ModelForm):
    payment = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Fee Payment'}),)
    dues = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Fee Payment'}),required=False)
    advance = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Fee Payment'}),required=False)
    class Meta():
        model = feeadd
        fields = ['payment','dues','advance',]