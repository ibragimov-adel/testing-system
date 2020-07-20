from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        max_length=30,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password1 = forms.CharField(
        label='Пароль',
        max_length=30,
        min_length=6,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password2 = forms.CharField(
        label='Повторите пароль',
        max_length=30,
        min_length=6,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    error_messages = {
        'password_mismatch': 'Пароли должны совпадать'
    }

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя',
        max_length=30,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        label='Пароль',
        max_length=30,
        min_length=6,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    error_messages = {
        'invalid_login': 'Неверное имя пользователя или пароль'
    }

    class Meta:
        model = User
        fields = ('username', 'password')
=======


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        exclude = ["passed_quantiry"]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = [""]
