from .models import *
from django.forms import ModelForm, TextInput, Textarea, ImageField
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class Art_form(ModelForm):
    class Meta:
        model = Art
        image_file = forms.ImageField()
        fields = ['title', 'genre', 'image_file', 'describition']

        widgets = {
            'title': TextInput(attrs={
                'class': 'name_of_art',
                'placeholder': 'Название'
            }),
            'genre': TextInput(attrs={
                'class': 'genre',
                'placeholder': 'Жанр'
            }),
            'describition': Textarea(attrs={
                'class': 'describition',
                'placeholder': 'Описание'
            }),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
