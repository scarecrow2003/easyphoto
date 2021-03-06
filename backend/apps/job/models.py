from django.db import models
from ..common.models import BaseModel


# Create your models here.
class EPJob(BaseModel):
    from ..workflow.models import EPWorkflow, EPStatus
    from ..account.models import EPCompany, EPAccount
    customer_name = models.CharField(max_length=30)
    customer = models.IntegerField(blank=True)
    company = models.ForeignKey(EPCompany)
    photo_date = models.DateTimeField(null=True, blank=True)
    workflow = models.ForeignKey(EPWorkflow)
    status = models.ForeignKey(EPStatus)
    assignments = models.ManyToManyField(EPAccount, through='EPTaskAssignment')

    class Meta:
        app_label = 'job'
        db_table = 'ep_job'


class EPTaskAssignment(BaseModel):
    from ..account.models import EPAccount
    from ..workflow.models import EPTask
    job = models.ForeignKey(EPJob)
    task = models.ForeignKey(EPTask)
    work = models.ForeignKey(EPAccount)
    remarks = models.CharField(max_length=100)

    class Meta:
        app_label = 'job'
        db_table = 'ep_task_assignment'

