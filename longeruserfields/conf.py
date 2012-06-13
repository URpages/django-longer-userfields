# encoding: utf-8
from appconf import AppConf

class ApplicationSettings(AppConf):
	""" Overridable Application Settings
		more info : https://github.com/jezdez/django-appconf """
	USERNAME_LENGTH = 36 # length of a UUID1
	EMAIL_LENGTH = 255 # maximum possible length of an email address

	class Meta:
		prefix = 'longeruserfields'