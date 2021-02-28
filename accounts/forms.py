from django import forms
from django.forms.widgets import EmailInput, PasswordInput, TextInput


class sign_inForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=TextInput(attrs={
            'name': 'username',
            'class': 'input100',
            'placeholder': 'Foydalanuvchi nomi(username)',
            'required': 'required'
        })
    )
    password = forms.CharField(
        widget=PasswordInput(attrs={
            'name': 'password',
            'class': 'input100',
            'placeholder': 'Parolingiz',
            'required': 'required'
        })
    )


class sign_upForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        widget=TextInput(attrs={
            'name': 'first_name',
            'class': 'input--style-4',
            'required': 'required'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        widget=TextInput(attrs={
            'name': 'last_name',
            'class': 'input--style-4',
            'required': 'required'
        })
    )
    email = forms.EmailField(
        widget=EmailInput(attrs={
            'name': 'email',
            'class': 'input--style-4',
            'required': 'required'
        })
    )
    username = forms.CharField(
        max_length=30,
        widget=TextInput(attrs={
            'name': 'username',
            'class': 'input--style-4',
            'required': 'required'
        })
    )
    password1 = forms.CharField(
        widget=PasswordInput(attrs={
            'name': 'password1',
            'class': 'input--style-4',
            'required': 'required'
        })
    )
    password2 = forms.CharField(
        widget=PasswordInput(attrs={
            'name': 'password2',
            'class': 'input--style-4',
            'required': 'required'
        })
    )
