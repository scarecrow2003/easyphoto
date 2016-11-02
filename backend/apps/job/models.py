from django.db import models
from apps.account.models import EPCompany
from apps.workflow.models import EPWorkflow
from apps.account.models import EPAccount
from apps.common.models import BaseModel


# Create your models here.
class EPJob(BaseModel):
    customer_name = models.CharField(max_length=30)
    customer_id = models.IntegerField(blank=True)
    company_id = models.ForeignKey(EPCompany)

    class Meta:
        app_label = 'job'
        db_table = 'ep_job'


class EPTask(BaseModel):
    task_name = models.CharField(max_length=30)
    workflow_id = models.ForeignKey(EPWorkflow)

    class Meta:
        app_label = 'job'
        db_table = 'ep_task'


class EPTaskAssignment(BaseModel):
    job_id = models.ForeignKey(EPJob)
    task_id = models.ForeignKey(EPTask)
    work_id = models.ForeignKey(EPAccount)
    remarks = models.CharField(max_length=100)

    class Meta:
        app_label = 'job'
        db_table = 'ep_task_assignment'

