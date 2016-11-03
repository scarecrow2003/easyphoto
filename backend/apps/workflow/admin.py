from django.contrib import admin
from .models import EPTask, EPStatus, EPWorkflow

# Register your models here.
admin.site.register(EPWorkflow)
admin.site.register(EPStatus)
admin.site.register(EPTask)
