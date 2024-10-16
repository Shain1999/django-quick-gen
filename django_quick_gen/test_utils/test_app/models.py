from django.db import models

from django_quick_gen.decorators import generate_resources

# Create your models here.
@generate_resources
class Test(models.Model):
    name =models.CharField(max_length=10)
