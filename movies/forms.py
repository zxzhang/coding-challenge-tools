'''
Created on May 3, 2015

@author: Polarbear
'''

from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    def clean_username(self):
        count = User.objects.filter(username = self.cleaned_data['username']).count()
        if count > 0:
            raise forms.ValidationError("User is exist.")
        return self.cleaned_data['username']

    def clean_email(self):
        count = User.objects.filter(email = self.cleaned_data['email']).count()
        if count > 0:
            raise forms.ValidationError("Email is exist.")
        return self.cleaned_data['email']

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        pw1 = cleaned_data.get('password1')
        pw2 = cleaned_data.get('password2')
        if pw1 and pw2 and pw1 != pw2:
            raise forms.ValidationError("password1 does not equal to password2")
        return cleaned_data
    
class SigninForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField()

class ResendEmailForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    def clean_email(self):
        count = User.objects.filter(email = self.cleaned_data['email']).count()
        if count == 0:
            raise forms.ValidationError("User does not exist.")
        return self.cleaned_data['email']

class ResetUserPassword(forms.Form):
    password1 = forms.CharField(label="Input New Password",widget=forms.TextInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Re-input New Password",widget=forms.TextInput(attrs={'class':'form-control'}))
    def clean(self):
        cleaned_data = super(ResetUserPassword, self).clean()
        pw1 = cleaned_data.get('password1')
        pw2 = cleaned_data.get('password2')
        if pw1 and pw2 and pw1 != pw2:
            raise forms.ValidationError("password1 does not equal to password2")
        return cleaned_data
    
class ForgetPasswordForm(forms.Form):
    email=forms.EmailField(max_length=80,widget=forms.TextInput(attrs={'class':'form-control'}))
    def clean_email(self):
        count = User.objects.filter(email = self.cleaned_data['email']).count()
        if count == 0:
            raise forms.ValidationError("User does not exist!")
        return self.cleaned_data['email']
