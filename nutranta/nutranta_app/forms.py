from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username' ,'email', 'password1', 'password2']
        labels = {'email': 'Email'} 
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}

class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'autofocus': True}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}))


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'}))

class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}))

class Contact_Us(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Phone', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Message', max_length=500, widget=forms.Textarea(attrs={'class': 'form-control'}) )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer 
        fields = ['name', 'email', 'mobile', 'locality', 'city', 'state', 'zipcode']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                    'locality': forms.TextInput(attrs={'class': 'form-control'}),
                    'city': forms.TextInput(attrs={'class': 'form-control'}),
                    'state': forms.Select(attrs={'class': 'form-control'}),
                    'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
                    'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
                    'email': forms.EmailInput(attrs={'class': 'form-control'})}

   


