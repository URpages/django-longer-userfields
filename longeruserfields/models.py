# encoding: utf-8

import django
from django.utils.translation import ugettext as _
from django.db.models.signals import class_prepared
from django.conf import settings

from .conf import ApplicationSettings


MAX_USERNAME_LENGTH = ApplicationSettings.USERNAME_LENGTH
MAX_EMAIL_LENGTH = ApplicationSettings.EMAIL_LENGTH


def extend_user_fields(sender, *args, **kwargs):
    if (sender.__name__ == "User" and
        sender.__module__ == "django.contrib.auth.models"):
        patch_user_model(sender)
class_prepared.connect(extend_user_fields)

def patch_user_model(model):
    #
    # Username
    #
    field_username = model._meta.get_field(fieldname)
    update_field_length(field_username, MAX_USERNAME_LENGTH)

    #
    # Email Address
    #
    field_emailaddress = model._meta.get_field(fieldname)
    update_field_length(field_username, MAX_EMAIL_LENGTH)


# https://github.com/GoodCloud/django-longer-username/issues/1
# django 1.3.X loads User model before class_prepared signal is connected
# so we patch model after it's prepared

from django.contrib.auth.models import User

# check if User model is patched
username_is_patched = User._meta.get_field("username").max_length == MAX_USERNAME_LENGTH
emailaddress_is_patched = User._meta.get_field("email").max_length == MAX_EMAIL_LENGTH

if not username_is_patched or not emailaddress_is_patched:
    patch_user_model(User)