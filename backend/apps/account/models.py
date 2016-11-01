from django.db import models
from django.contrib.auth.models import User


class EPAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=30)

    class Meta:
        app_label = 'account'

    def __str__(self):
        return self.nick_name
