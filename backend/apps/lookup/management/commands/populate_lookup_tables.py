from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.auth.models import Group
from apps.account.models import EPCompany, EPPosition
from apps.workflow.models import EPWorkflow
from apps.job.models import EPTask


class Command(BaseCommand):
    POSITIONS = [
        ('FRONT', 'Front desk admin'),
        ('PHOTO', 'Photographer'),
        ('MKUP', 'Makeup artist'),
        ('DESIGN', 'Graphic Designer'),
        ('HELPER', 'Photographer help')
    ]

    TASKS = [
        ('REGIS', 'Register the customer'),
        ('MAKEUP', 'Do makeup for the customer'),
        ('SHOOT', 'Do photo shoot for the customer'),
        ('LIGHT', 'Lightly touch up the photos'),
        ('CHOOSE', 'Do photo selection with customer'),
        ('TOUCHUP', 'Do final touch up of the photos'),
        ('SEND', 'Send photos to vendor to printing'),
        ('RECEIVE', 'Printed photos received from vendor and CD burned'),
        ('DONE', 'Photos collected by customer')
    ]

    @transaction.atomic
    def handle(self, *args, **options):
        if Group.objects.all().count() == 0 and EPCompany.objects.all().count() == 0:
            group = Group.objects.create(name='easyphoto')
            company = EPCompany.objects.create(group=group, company_name='easyphoto')
        if EPPosition.objects.all().count() == 0:
            for name, description in Command.POSITIONS:
                EPPosition.objects.create(company_id=company, name=name, description=description)
        if EPWorkflow.objects.all().count() == 0:
            EPWorkflow.objects.create(workflow_name='epworkflow', company_id=1)
        if EPTask.objects.all().count() == 0:
            for name, description in Command.TASKS:
                EPTask.objects.create(workflow_name=name, description=description, company_id=1)
