from gameServer.settings import AUTH_PASSWORD_VALIDATORS
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation
from django import forms

class ResetForm(PasswordResetForm):
    email = forms.EmailField(
        label='',
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", 'placeholder': 'Email'}),
    )

class RecoverPassword(SetPasswordForm):
    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': 'Password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': 'Confirm password'}),
    )
    
