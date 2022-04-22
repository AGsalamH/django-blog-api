import uuid
from django.db import models

# Create your models here.

class BaseModel(models.Model):
    '''Base setup for all model'''
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
