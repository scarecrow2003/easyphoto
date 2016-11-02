from django.db import models
from apps.account.models import EPCompany
from apps.common.models import BaseModel


# Create your models here.
class EPWorkflow(BaseModel):
    workflow_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)
    company_id = models.ForeignKey(EPCompany)

    class Meta:
        app_label = 'workflow'
        db_table = 'workflow'
