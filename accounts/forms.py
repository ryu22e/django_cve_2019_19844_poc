from django import forms
from django.contrib.auth.forms import PasswordResetForm


class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Don't use EmailInput. Because 'mıke@example.org' cannot be entered.
        self.fields['email'].widget = forms.TextInput()
