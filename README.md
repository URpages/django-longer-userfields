`django-longer-userfields` provides a migration and a monkeypatch for the django auth.user model to allow customisable field lengths for usernames and email addresses.

It's designed to be a simple include-and-forget project that makes a little headache go away.  Enjoy, and pull requests welcome!

Usage
=====
Step 1. Install django-longer-userfields.
-------------------------------------

- `pip install longeruserfields`

You will also need to install [south]() to use the migration.

 - `pip install south`


Step 2. Add `longeruserfields` to your installed apps.
-------------------------
Add 'longeruserfields' to the top of your `INSTALLED_APPS` in settings.py

settings.py

```python
INSTALLED_APPS = ("longeruserfields",) + INSTALLED_APPS
```

Step 3. (Optional) Specify a custom username length
------------------------------------------------
If you want to specify a custom length, add it to settings.py. The default is 36.

settings.py

```python
LONGERUSERFIELDS_USERNAMELENGTH = 75  # optional, default is 36.
```

Step 4. (Optional) Specify a custom email length
------------------------------------------------
If you want to specify a custom length, add it to settings.py. The default is 255 characters.

settings.py

```python
LONGERUSERFIELDS_EMAILLENGTH = 100  # optional, default is 255.
```


Step 4. Run the migration
------------------------------------------------
```
$ python manage.py migrate longeruserfields
```

That's it, you should be good to go!


Notes about the built-in forms
==============================
This app also automatically monkey patches the User forms in the Django admin to remove the 30 character limit for usernames and the 75 character limite for email addresses.

It provides a suitable replacement for the standard AuthenticationForm as well, but due to the implementation you must manually utilize it.

urls.py

```python
from longeruserfields.forms import AuthenticationForm

urlpatterns = patterns('',
    # ...
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'authentication_form': AuthenticationForm}),
)
```

Credits
=======

The monkeypatch for this is very largely based on [celement's answer on stackoverflow](http://stackoverflow.com/questions/2610088/can-djangos-auth-user-username-be-varchar75-how-could-that-be-done)

This has been forked and improved upon based on [madssj](http://pypi.python.org/pypi/django-longerusernameandemail/0.5.2) implementation.


Todo
====

Implement a way to allow usage of custom model for users