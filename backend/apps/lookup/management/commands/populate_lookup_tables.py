from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.auth.models import Group, User
from ....account.models import EPCompany, EPPosition, EPAccountCompany, EPAccount
from ....workflow.models import EPWorkflow, EPStatus, EPTask


class Command(BaseCommand):
    POSITIONS = [
        ('FRONT', 'Front desk admin'),
        ('PHOTO', 'Photographer'),
        ('MKUP', 'Makeup artist'),
        ('DESIGN', 'Graphic Designer'),
        ('HELPER', 'Photographer help'),
        ('GENERAL', 'General position')
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

    STATUS = [
        (1, 'Registered', 'REGIS'),
        (2, 'Makeup Started', 'MAKEUP'),
        (3, 'Makeup done', 'MAKEUP'),
        (4, 'Photo shoot started', 'SHOOT'),
        (5, 'Photo shoot done', 'SHOOT'),
        (6, 'Lightly touch up done', 'LIGHT'),
        (7, 'Photo selection start', 'CHOOSE'),
        (8, 'Photo selection done', 'CHOOSE'),
        (9, 'Touch up start', 'TOUCHUP'),
        (10, 'Touch up done', 'TOUCHUP'),
        (11, 'Send to vendor to print', 'SEND'),
        (12, 'Printed photo returned', 'RECEIVE'),
        (13, 'Customer collected', 'DONE')
    ]

    @transaction.atomic
    def handle(self, *args, **options):
        if Group.objects.all().count() == 0 and EPCompany.objects.all().count() == 0:
            group = Group.objects.create(name='easyphoto')
            company = EPCompany.objects.create(group=group, company_name='easyphoto')
            # for test only
            account = EPAccount.objects.create(user=User.objects.get(pk=1), nick_name='Nicolas')
            member = EPAccountCompany(account=account, company=company)
            member.save()
        if EPPosition.objects.all().count() == 0:
            company = EPCompany.objects.get(pk=1)
            for name, description in Command.POSITIONS:
                EPPosition.objects.create(company=company, name=name, description=description)
        if EPWorkflow.objects.all().count() == 0:
            company = EPCompany.objects.get(pk=1)
            EPWorkflow.objects.create(workflow_name='epworkflow', company=company)
        if EPTask.objects.all().count() == 0:
            workflow = EPWorkflow.objects.get(pk=1)
            for name, description in Command.TASKS:
                EPTask.objects.create(workflow=workflow, task_name=name, description=description)
        if EPStatus.objects.all().count() == 0:
            workflow = EPWorkflow.objects.get(pk=1)
            for sequence, name, task in Command.STATUS:
                task = EPTask.objects.get(task_name=task)
                EPStatus.objects.create(sequence=sequence, name=name, workflow=workflow, task=task)
