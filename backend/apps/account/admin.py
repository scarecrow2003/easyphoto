from django.contrib import admin
from .models import EPAccount, EPCompany

# Register your models here.
admin.site.register(EPAccount)
admin.site.register(EPCompany)