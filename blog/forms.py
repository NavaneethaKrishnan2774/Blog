from django import forms

class contactform(forms.Form):
    name = forms.forms.CharField(label='name', max_length= 100)
    email = forms.EmailField(label='email')
    message = forms.CharField(label='message')