from django.contrib.auth.models import User

class AccountModel(models.Model):
    user = models.OneToOneField(User, on_delect=model.CASCADE)
    nick_name = models.CharField(max_length=30)