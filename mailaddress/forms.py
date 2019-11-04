from django import forms
from .models import *

from ckeditor.widgets import CKEditorWidget
class mailaddress1(forms.ModelForm):
    to = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                                )
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',}),)
    body = forms.CharField(widget=CKEditorWidget(attrs={'ckeditor': {'width': '40%', 'height': '400px'}}))


    class Meta():
        model = mailaddress
        fields = ['to', 'subject', 'body' ]