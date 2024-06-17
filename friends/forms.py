from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from friends.models import *

class UserForm(forms.ModelForm):
    re_email = forms.EmailField(label='Confirm Email')
    re_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username','email','password']
        widgets = {
            'password': forms.PasswordInput,
        }
        labels = {
            'email': 'Email',
            'password': 'Password'
        }
        help_texts = {
            'password': 'Password must be at least 8 characters long and include:',
            }
        
    def clean_email(self):
        email = self.cleaned_data.get('email')  # Ensure this matches the case used in the form
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("Invalid email format")
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        re_email = cleaned_data.get('re_email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if email and re_email and email != re_email:
            self.add_error('re_email', "Emails do not match")

        if password and re_password and password != re_password:
            self.add_error('re_password', "Passwords do not match")
            
        if password:
            try:
                validate_password(password)
            except ValidationError as e:
                self.add_error('Password', e)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile_class
        fields = ['profile_pic']


class FriendRequestForm(forms.ModelForm):
    class Meta:
        model = Frined_request_class
        fields = '__all__'
