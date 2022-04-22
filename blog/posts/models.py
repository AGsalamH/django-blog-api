from django.db import models
from django.conf import settings
from blog.core.models import BaseModel

# Create your models here.

class Post(BaseModel):
    title = models.CharField(max_length=120)
    content = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
