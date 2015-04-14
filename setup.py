#!/usr/bin/env python

from setuptools import setup

setup(
name='django-fanout',
version='1.1.1',
description='Fanout.io library for Django',
author='Justin Karneges',
author_email='justin@fanout.io',
url='https://github.com/fanout/django-fanout',
license='MIT',
py_modules=['django_fanout'],
install_requires=['fanout>=1.1.1'],
classifiers=[
	'Topic :: Utilities',
	'License :: OSI Approved :: MIT License'
]
)
