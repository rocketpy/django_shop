from django import forms
from . import *


class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

        class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'password')
