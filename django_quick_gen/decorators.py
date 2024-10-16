# utils/decorators.py
from rest_framework import serializers, viewsets
from django.contrib import admin
from .apps import DjangoQuickGenConfig

def generate_resources(decorated_model):
    """Automatically generate serializer, viewset, and admin registration."""
    
    # Create a Serializer for the model dynamically
    class Meta:
        model = decorated_model
        fields = "__all__"

    serializer = type(f"{decorated_model.__name__}Serializer", (serializers.ModelSerializer,), {"Meta": Meta})
    
    # Create a ViewSet for the model dynamically
    viewset = type(
        f"{decorated_model.__name__}ViewSet",
        (viewsets.ModelViewSet,),
        {"queryset": decorated_model.objects.all(), "serializer_class": serializer},
    )
    
    # Register the model in the Django admin dynamically
    admin.site.register(decorated_model)

    # Store the generated resources on the model class for easy access
    decorated_model._generated_serializer = serializer
    decorated_model._generated_viewset = viewset

    # Register the viewset with the router
    DjangoQuickGenConfig.dynamic_router.register(decorated_model.__name__.lower(), viewset)  # Register with a lowercase name

    return decorated_model
