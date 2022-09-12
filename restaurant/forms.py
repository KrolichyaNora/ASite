from django import forms

class AuthDataForm(forms.Form):
    login = forms.CharField(max_length=32, required=True)
    password = forms.CharField(max_length=64, required=True)