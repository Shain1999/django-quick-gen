#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-quick-gen
------------

Tests for `django-quick-gen` models module.
"""

from django.test import TestCase
# tests/test_models.py
from django.test import TestCase
from django.urls import reverse
from django_quick_gen.test_utils.test_app.models import Test

class TestGenerateResourcesDecorator(TestCase):
    
    def setUp(self):
        # Create a Test instance
        self.test_instance = Test.objects.create(name="Sample")

    def test_model_creation(self):
        # Check if the model instance was created successfully
        self.assertIsNotNone(self.test_instance.pk)

    def test_api_test_viewset(self):
        from django.conf import settings  # Import settings
        NAMESPACE = settings.DQG_SETTINGS.get("NAMESPACE", "api")

        # Make a request to the API endpoint
        url = reverse(f'{NAMESPACE}:test-list')  # Adjust the name according to your URL configuration
        
        # Retrieve the list of Test instances
        response = self.client.get(url)
        
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check if the response data contains the created Test instance
        self.assertIn({"id": self.test_instance.id, "name": "Sample"}, response.json())
