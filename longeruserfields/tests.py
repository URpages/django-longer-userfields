from django.contrib.auth.models import User
from django.test import TestCase

from .conf import ApplicationSettings

MAX_USERNAME_LENGTH = ApplicationSettings.USERNAME_LENGTH
MAX_EMAIL_LENGTH = ApplicationSettings.EMAIL_LENGTH


class LongerUserFieldsTests(TestCase):
    """
    Unit tests for longerusername app
    """
    def setUp(self):
        """
        creates a user with a terribly long username
        """
        long_username = 'a'*MAX_USERNAME_LENGTH
        long_emailaddress = 'a'*(MAX_EMAIL_LENGTH-6) + "@a.com"

        self.user = User(username='test' + long_username,
                         email=long_emailaddress,
                         password='testpassword')
        self.user.save();

    def testUserCreation(self):
        """
        tests that self.user was successfully saved, and can be retrieved
        """
        self.assertNotEqual(self.user,None)
        User.objects.get(id=self.user.id) # returns DoesNotExist error if the user wasn't created