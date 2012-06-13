# encoding: utf-8
import datetime

from south.db import db
from south.v2 import SchemaMigration
from django.db import models

from ..conf import ApplicationSettings


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.alter_column('auth_user', 'username', models.CharField(max_length=ApplicationSettings.USERNAME_LENGTH))
        db.alter_column('auth_user', 'email', models.EmailField(max_length=ApplicationSettings.EMAIL_LENGTH))

    def backwards(self, orm):
        db.alter_column('auth_user', 'username', models.CharField(max_length=30))
        db.alter_column('auth_user', 'email', models.EmailField(max_length=75))

