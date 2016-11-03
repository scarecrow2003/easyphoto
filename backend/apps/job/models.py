from django.db import models
from ..common.models import BaseModel


# Create your models here.
class EPJob(BaseModel):
    from ..workflow.models import EPWorkflow, EPStatus
    from ..account.models import EPCompany
    customer_name = models.CharField(max_length=30)
    customer_id = models.IntegerField(blank=True)
    company_id = models.ForeignKey(EPCompany)
    photo_date = models.DateTimeField(null=True, blank=True)
    workflow_id = models.ForeignKey(EPWorkflow)
    status = models.ForeignKey(EPStatus)

    class Meta:
        app_label = 'job'
        db_table = 'ep_job'


class EPTaskAssignment(BaseModel):
    from ..account.models import EPAccount
    from ..workflow.models import EPTask
    job_id = models.ForeignKey(EPJob)
    task_id = models.ForeignKey(EPTask)
    work_id = models.ForeignKey(EPAccount)
    remarks = models.CharField(max_length=100)

    class Meta:
        app_label = 'job'
        db_table = 'ep_task_assignment'

