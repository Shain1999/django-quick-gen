# -*- coding: utf-8
from django.apps import AppConfig
from rest_framework.routers import DefaultRouter
from django.conf import settings  # Import settings



class DjangoQuickGenConfig(AppConfig):
    name = 'django_quick_gen'
    dynamic_router = DefaultRouter()  # Create a router instance
        
    # Class properties for settings
    ROUTE_PREFIX = settings.DQG_SETTINGS.get("ROUTE_PREFIX", "api")
    NAMESPACE = settings.DQG_SETTINGS.get("NAMESPACE", "api")

    @classmethod
    def get_router_urls(cls):
        """Returns the URLs registered in the dynamic router prefixed with /api/."""
        return cls.dynamic_router.urls
