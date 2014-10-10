#!/usr/bin/env python

from setuptools import setup

setup(
name='django-fanout',
version='1.0.0',
description='Fanout.io library for Django',
author='Justin Karneges',
author_email='justin@fanout.io',
url='https://github.com/fanout/django-fanout',
license='MIT',
py_modules=['django_fanout'],
install_requires=['pyfanout>=1.0.0'],
classifiers=[
	'Topic :: Utilities',
	'License :: OSI Approved :: MIT License'
]
)
