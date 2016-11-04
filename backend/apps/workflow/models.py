from django.db import models
from ..common.models import BaseModel


# Create your models here.
class EPWorkflow(BaseModel):
    from ..account.models import EPCompany
    workflow_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)
    company = models.ForeignKey(EPCompany)

    class Meta:
        app_label = 'workflow'
        db_table = 'ep_workflow'


class EPTask(BaseModel):
    task_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True)
    workflow = models.ForeignKey(EPWorkflow)

    class Meta:
        app_label = 'workflow'
        db_table = 'ep_task'


class EPStatus(BaseModel):
    workflow = models.ForeignKey(EPWorkflow)
    sequence = models.IntegerField()
    name = models.CharField(max_length=100)
    task = models.ForeignKey(EPTask)

    class Meta:
        app_label = 'workflow'
        db_table = 'ep_status'
