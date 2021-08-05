from django import forms
class signupForm(forms.Form):
    name=forms.CharField()
    uname=forms.CharField()
    email=forms.CharField()
    phone=forms.CharField()
    pas=forms.CharField(widget=forms.PasswordInput)
    confpas=forms.CharField(widget=forms.PasswordInput)
    agree=forms.BooleanField()
class suggForm(forms.Form):
    suggestion=forms.CharField()

class loginForm(forms.Form):
    loginname=forms.CharField()
    loginpass=forms.CharField(widget=forms.PasswordInput)
class userworkForm(forms.Form):
    addphoto=forms.FileField()
