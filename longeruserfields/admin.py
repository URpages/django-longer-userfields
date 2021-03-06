# encoding: utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .forms import UserCreationForm, UserChangeForm
from .conf import ApplicationSettings

class LongerUserNameUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm

admin.site.unregister(User)
admin.site.register(User, LongerUserNameUserAdmin)
