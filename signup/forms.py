from django import forms

class userDetails(forms.Form):
    email = forms.EmailField(label="Enter your email address here: ")
    username = forms.CharField(label="Enter your username here: ", max_length=20)
    password = forms.CharField(label="Enter your password here: ", widget=forms.PasswordInput)
    confirmPassword = forms.CharField(label="Enter your password here: ", widget=forms.PasswordInput)