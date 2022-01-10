from django.forms import forms,ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

class UserForm(UserCreationForm):
    name = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=50)
    image = forms.ImageField()
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2']
class register(UserCreationForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-conntrol',
                   'placeholder':'FIO'}
        ),
        max_length=200,
        localize=True
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-conntrol',
                   'placeholder':'number'}
        ),
        max_length=50,
        localize=True
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-conntrol',
                   'placeholder':'Username'}
        ),
        max_length=200,
        localize=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class':'form-control',
                   'placeholder':'Parolingiz'}
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={'class':'form-control',
                   'placeholder':'Email manzilingiz'}
        )
    )



