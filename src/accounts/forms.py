from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')


class ProfileFrom(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('image', 'account_type', 'city',
                  'address', 'Mobail', 'subject', 'year', "description", 'school_name')


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('image', 'city', 'address', 'Mobail',
                  'subject', 'year', "description", 'school_name')
