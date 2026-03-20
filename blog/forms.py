from django import forms
from django.contrib.auth.models import User
class contactform(forms.Form):
    name = forms.CharField(label='name', max_length= 100,required=True)
    email = forms.EmailField(label='email',required=True)
    message = forms.CharField(label='message',required=True)

class registerform(forms.ModelForm):
    username = forms.CharField(label='username',max_length=100,required=False)
    email = forms.EmailField(label='email',required=True)
    password= forms.CharField(label='password',max_length=100,required=True)
    confirmpassword= forms.CharField(label='confirmpassword',max_length=100,required=True)

    class Meta:
        model = User
        fields =["username","email","password"]

    def clean (self):
        cleaned_data=super().clean()
        password=cleaned_data.get("password")
        confirmpassword=cleaned_data.get("confirmpassword")

        if password and confirmpassword and password != confirmpassword:
            raise forms.ValidationError("password mismatch")
