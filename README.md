Django-Fanout
-------------
Author: Justin Karneges <justin@fanout.io>

Fanout.io library for Python/Django.

Requirements
------------

* pyfanout

Install
-------

You can install from PyPi:

    sudo pip install django-fanout

Or from this repository:

    sudo python setup.py install

Sample usage
------------

Put your Fanout.io credentials in settings.py:

```python
FANOUT_REALM = 'my-realm-id'
FANOUT_KEY = 'my-realm-key'
```

Then you can publish JSON objects from anywhere in your project:

```python
import django_fanout as fanout

fanout.publish('some-channel', 'hello')
```
