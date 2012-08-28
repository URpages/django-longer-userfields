# encoding: utf-8

import django
from django.utils.translation import ugettext as _
from django.db.models.signals import class_prepared
from django.conf import settings

from .conf import ApplicationSettings
from .utils import update_field_length

MAX_USERNAME_LENGTH = ApplicationSettings.USERNAME_LENGTH
MAX_EMAIL_LENGTH = ApplicationSettings.EMAIL_LENGTH


def patch_user_model(model):
    # check if User model is patched
    if not model._meta.get_field("username").max_length == MAX_USERNAME_LENGTH:
        update_field_length(model._meta.get_field("username"), MAX_USERNAME_LENGTH)

    if not model._meta.get_field("email").max_length == MAX_EMAIL_LENGTH:
        update_field_length(model._meta.get_field("email"), MAX_EMAIL_LENGTH)

def extend_user_fields(sender, *args, **kwargs):
    if (sender.__name__ == "User" and sender.__module__ == "django.contrib.auth.models"):
        patch_user_model(sender)
class_prepared.connect(extend_user_fields)



# https://github.com/GoodCloud/django-longer-username/issues/1
# django 1.3.X loads User model before class_prepared signal is connected
# so we patch model after it's prepared
from django.contrib.auth.models import User
patch_user_model(User)
