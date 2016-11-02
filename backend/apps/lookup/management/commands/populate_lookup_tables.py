from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.auth.models import Group
from apps.account.models import EPCompany, EPPosition


class Command(BaseCommand):
    POSITIONS = [
        ('FRONT', 'Front desk admin'),
        ('PHOTO', 'Photographer'),
        ('MKUP', 'Makeup artist'),
        ('DESIGN', 'Graphic Designer'),
        ('HELPER', 'Photographer help')
    ]

    @transaction.atomic
    def handle(self, *args, **options):
        if Group.objects.all().count() == 0 and EPCompany.objects.all().count() == 0:
            group = Group.objects.create(name='easyphoto')
            company = EPCompany.objects.create(group=group, company_name='easyphoto')
            if EPPosition.objects.all().count() == 0:
                for name, description in Command.POSITIONS:
                    EPPosition.objects.create(company_id=company, name=name, description=description)