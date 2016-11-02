from django.db import models


# Create your models here.
class BaseModel(models.Model):
    defunct = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        app_label = 'common'
