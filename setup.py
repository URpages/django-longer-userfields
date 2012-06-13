#/usr/bin/env python
import os
from setuptools import (
  setup,
  find_packages,
)
import longeruserfields

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
    name = "longeruserfields",
    version = longeruserfields.__version__,
    classifiers = (
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ),

    author='URpages Pty Ltd',
    author_email='developers@urpages.net',
    url='http://github.com/URpages/django-longer-userfields',

    description='Django application which allows for customisable field user field lengths',
    long_description = read('README.md'),

    packages = find_packages(),
    install_requires=(
        'django-appconf==0.4.1',
        'South==0.7.5',
    ),
    zip_safe = False,
)
