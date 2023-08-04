from django import forms
from django.forms import ModelForm, Form, Textarea
from django.forms.fields import EmailField

class ContactForm(Form):

    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=Textarea)
