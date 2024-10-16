=====
Usage
=====

To use DjangoQuickGen in a project, add it to your `INSTALLED_APPS`:

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
