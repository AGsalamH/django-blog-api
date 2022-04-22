from django.db import models
from django.contrib.auth.models import AbstractUser 

from blog.core.models import BaseModel

# Create your models here.

class User(AbstractUser, BaseModel):
    '''All Users are represented by this model'''
    pass
