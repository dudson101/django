from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required="false")

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
