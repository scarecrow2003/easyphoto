from django.db import models
from django.contrib.auth.models import User, Group


class EPAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=30)
    wechat_id = models.CharField(max_length=50, blank=True)

    class Meta:
        app_label = 'account'
        db_table = 'account'

    def __str__(self):
        return self.nick_name


class EPCompany(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)

    class Meta:
        app_label = 'account'
        db_table = 'company'

    def __str__(self):
        return self.company_name
