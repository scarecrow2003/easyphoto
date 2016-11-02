from django.db import models
from django.utils import timezone


# Create your models here.
class BaseModel(models.Model):
    defunct = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
        app_label = 'common'
