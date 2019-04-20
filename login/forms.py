from django import forms

class usernamePassword(forms.Form):
    username = forms.CharField(label = "Enter your name here: ", max_length=20)
    password = forms.CharField(label = "Enter your password here: ", widget=forms.PasswordInput)