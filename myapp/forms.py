from django.forms import ModelForm
from .models import Notes
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class NoteForm(ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']