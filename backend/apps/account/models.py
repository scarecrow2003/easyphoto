from django.db import models
from django.contrib.auth.models import User, Group
from apps.common.models import BaseModel


class EPAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=30)
    wechat_id = models.CharField(max_length=50, blank=True)

    class Meta:
        app_label = 'account'
        db_table = 'ep_account'

    def __str__(self):
        return self.nick_name


class EPCompany(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)

    class Meta:
        app_label = 'account'
        db_table = 'ep_company'

    def __str__(self):
        return self.company_name


class EPPosition(BaseModel):
    company_id = models.ForeignKey(EPCompany)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    class Meta:
        app_label = 'account'
        db_table = 'ep_position'

    def __str__(self):
        return self.title


class EPAccountCompany(BaseModel):
    account_id = models.ForeignKey(EPAccount)
    company_id = models.ForeignKey(EPCompany)
    position_id = models.ForeignKey(EPPosition)
    dividend = models.DecimalField(max_digits=4, decimal_places=2, default=2)

    class Meta:
        app_label = 'account'
        db_table = 'ep_account_company'

    def __str__(self):
        return self.account_id + self.company_id + self.position_id
