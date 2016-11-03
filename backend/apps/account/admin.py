from django.contrib import admin
from .models import EPAccount, EPCompany, EPPosition, EPAccountCompany

# Register your models here.
admin.site.register(EPAccount)
admin.site.register(EPCompany)
admin.site.register(EPPosition)
admin.site.register(EPAccountCompany)
