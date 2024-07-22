from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')  # Incluye el campo de correo electrónico

    def save(self, commit=True):
        user = super(UserCreationFormWithEmail,self).save(commit=False)
        if commit:
            user.save()
        return user
