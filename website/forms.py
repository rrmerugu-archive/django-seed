__author__ = 'rrmerugu'

from django import forms
from core.models import MyUser
from django.utils.translation import ugettext_lazy as _


class RegistrationForm(forms.Form):
    first_name = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("First Name"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.EmailInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Confirm Password"))

    def clean_email(self):
        try:
            user = MyUser.objects.get(email__iexact=self.cleaned_data['email'])
        except MyUser.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(_("The email already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
