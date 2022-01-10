from django import forms
from .models import Login



class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control',
                   'placeholder':'Username'}
        ),
        max_length=150
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'parol'})
    )