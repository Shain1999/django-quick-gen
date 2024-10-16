# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import


from django.urls import include, path

from django.contrib import admin

from django_quick_gen.urls import urlpatterns as dqg_urls


urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += dqg_urls
