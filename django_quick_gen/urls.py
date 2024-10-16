# -*- coding: utf-8 -*-
from django.urls import include, path
from .apps import DjangoQuickGenConfig


urlpatterns = [
    path(f'{DjangoQuickGenConfig.ROUTE_PREFIX}/',include((DjangoQuickGenConfig.get_router_urls(),DjangoQuickGenConfig.ROUTE_PREFIX),namespace=DjangoQuickGenConfig.NAMESPACE)),
]

