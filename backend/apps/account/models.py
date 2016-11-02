from django.db import models
from django.contrib.auth.models import User, Group


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


class EPPosition(models.Model):
    company_id = models.ForeignKey(EPCompany)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    class Meta:
        app_label = 'account'
        db_table = 'ep_position'

    def __str__(self):
        return self.title


class EPAccountCompany(models.Model):
    account_id = models.ForeignKey(EPAccount)
    company_id = models.ForeignKey(EPCompany)
    position_id = models.ForeignKey(EPPosition)

    class Meta:
        app_label = 'account'
        db_table = 'ep_account_company'

    def __str__(self):
        return self.account_id + self.company_id + self.position_id
