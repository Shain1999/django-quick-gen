=============================
DjangoQuickGen
=============================

.. image:: https://badge.fury.io/py/django-quick-gen.svg
    :target: https://badge.fury.io/py/django-quick-gen

.. image:: https://travis-ci.org/Shain1999/django-quick-gen.svg?branch=master
    :target: https://travis-ci.org/Shain1999/django-quick-gen

.. image:: https://codecov.io/gh/Shain1999/django-quick-gen/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/Shain1999/django-quick-gen

DjangoQuickGen is a Django package that simplifies API development by automatically generating serializers, viewsets, and admin registrations for your models. With a single decorator, transform your models into functional API endpoints, saving you time and effort while focusing on your application's logic.

Documentation
-------------

The full documentation is at https://django-quick-gen.readthedocs.io.

Quickstart
----------

Install DjangoQuickGen::

    pip install django-quick-gen

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_quick_gen.apps.DjangoQuickGenConfig',
        ...
    )

Add DjangoQuickGen's URL patterns:

.. code-block:: python

    from django_quick_gen import urls as django_quick_gen_urls


    urlpatterns = [
        ...
        url(r'^', include(django_quick_gen_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
