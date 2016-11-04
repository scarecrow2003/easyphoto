from django.db import models
from ..common.models import BaseModel


class EPAccount(models.Model):
    from django.contrib.auth.models import User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=30)
    wechat_id = models.CharField(max_length=50, blank=True)

    class Meta:
        app_label = 'account'
        db_table = 'ep_account'

    def __str__(self):
        return self.nick_name


class EPCompany(models.Model):
    from django.contrib.auth.models import Group
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    members = models.ManyToManyField(EPAccount, through='EPAccountCompany', related_name='companies')

    class Meta:
        app_label = 'account'
        db_table = 'ep_company'

    def __str__(self):
        return self.company_name


class EPPosition(BaseModel):
    company = models.ForeignKey(EPCompany)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    class Meta:
        app_label = 'account'
        db_table = 'ep_position'

    def __str__(self):
        return self.name


class EPAccountCompany(BaseModel):
    account = models.ForeignKey(EPAccount, on_delete=models.CASCADE)
    company = models.ForeignKey(EPCompany, on_delete=models.CASCADE)
    position = models.ForeignKey(EPPosition, blank=True, null=True)
    dividend = models.DecimalField(max_digits=4, decimal_places=2, default=2)
    max_discount = models.DecimalField(max_digits=4, decimal_places=2, default=20)
    salary = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        app_label = 'account'
        db_table = 'ep_account_company'

    def __str__(self):
        return self.account + self.company + self.position
