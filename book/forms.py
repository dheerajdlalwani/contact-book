from .models import *
from django.forms import ModelForm
from django import forms

class NewContactForm(ModelForm):
    firstName  = forms.CharField(label="First Name" ,widget=forms.TextInput(attrs={'class': 'inputBox', 'placeholder':'Joe'}))
    middleName  = forms.CharField(label="Middle Name", required=False ,widget=forms.TextInput(attrs={'class': 'inputBox', 'placeholder':'Robinette'}))
    lastName  = forms.CharField(label="Last Name", required=False ,widget=forms.TextInput(attrs={'class': 'inputBox', 'placeholder':'Biden'}))
    contact1  = forms.CharField(label="Contact 1" ,widget=forms.TextInput(attrs={'class': 'inputBox', 'placeholder':'987654321'}))
    contact2  = forms.CharField(label="Contact 2", required=False ,widget=forms.TextInput(attrs={'class': 'inputBox', 'placeholder':'987654321'}))
    email  = forms.EmailField(label="Email", required=False ,widget=forms.TextInput(attrs={'class': 'inputBox', 'placeholder':'someone@example.com'}))
    address  = forms.CharField(label="Address", required=False ,widget=forms.Textarea(attrs={'class': 'inputBox', 'placeholder':'6, New Avenue, XYZ Apt.'}))
    group  = forms.CharField(label="Group" ,widget=forms.Select(choices = CHOICES, attrs={'class': 'inputBox', 'placeholder':'Joe'}))
    favourite  = forms.BooleanField(label="Add to Favourites", required=False ,widget=forms.CheckboxInput())
    class Meta:
        model = Contact
        fields = "__all__"