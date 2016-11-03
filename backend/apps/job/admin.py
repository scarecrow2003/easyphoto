from django.contrib import admin
from .models import EPJob, EPTaskAssignment

# Register your models here.
admin.site.register(EPJob)
admin.site.register(EPTaskAssignment)
