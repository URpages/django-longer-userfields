from django.utils.translation import ugettext as _
from django.contrib.auth import forms as auth_forms
from django import forms

from .conf import ApplicationSettings
from .utils import update_field_length


MAX_USERNAME_LENGTH = ApplicationSettings.USERNAME_LENGTH
MAX_EMAIL_LENGTH = ApplicationSettings.EMAIL_LENGTH

class ExtendedFieldFormMixin(object):
    def __init__(self, *args, **kwargs):
        super(ExtendedFieldFormMixin, self).__init__(*args, **kwargs)
        username_field = self.fields.get('username', None)
        email_field = self.fields.get('email', None)
        if username_field and email_field:
            update_field_length(username_field, MAX_USERNAME_LENGTH)
            update_field_length(email_field, MAX_EMAIL_LENGTH)


class UserCreationForm(ExtendedFieldFormMixin, auth_forms.UserCreationForm): pass

class UserChangeForm(ExtendedFieldFormMixin, auth_forms.UserChangeForm): pass

class AuthenticationForm(ExtendedFieldFormMixin, auth_forms.AuthenticationForm): pass
