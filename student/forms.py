from django import forms
from .models import *

gender_choice = [('M', 'Male'), ('F', 'Female')]


class NewStudentForm(forms.ModelForm):
    FirstName = forms.CharField(widget=forms.TextInput(), required=True, max_length=20)
    LastName = forms.CharField(widget=forms.TextInput(), required=True, max_length=20)
    # DateOfBirth = forms.DateField(widget=forms.AdminDateWidget,required=True)
    Gaurdain = forms.CharField(widget=forms.TextInput(), required=True, max_length=20)
    MailingAddress = forms.CharField(widget=forms.TextInput(), required=True, max_length=20)
    occupation = forms.CharField(widget=forms.TextInput(), required=True, max_length=20)
    # PhoneNumber = forms.IntegerField(widget=forms.TextInput(),required=True,max_length=10)

    gender = forms.CharField(widget=forms.RadioSelect(choices=gender_choice))

    class Meta():
        model = student_detail
        fields = ['FirstName', 'LastName', 'gender']
