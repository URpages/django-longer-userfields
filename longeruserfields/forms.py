from django.utils.translation import ugettext as _
from django.contrib.auth import forms as auth_forms
from django import forms

from .conf import ApplicationSettings
from .utils import update_field_length


MAX_USERNAME_LENGTH = ApplicationSettings.USERNAME_LENGTH
MAX_EMAIL_LENGTH = ApplicationSettings.EMAIL_LENGTH


class UserCreationForm(auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        update_field_length(self.fields['username'], MAX_USERNAME_LENGTH)
        update_field_length(self.fields['email'], MAX_EMAIL_LENGTH)

class UserChangeForm(auth_forms.UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        update_field_length(self.fields['username'], MAX_USERNAME_LENGTH)
        update_field_length(self.fields['email'], MAX_EMAIL_LENGTH)

class AuthenticationForm(auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        update_field_length(self.fields['username'], MAX_USERNAME_LENGTH)
        update_field_length(self.fields['email'], MAX_EMAIL_LENGTH)
