from django.db import models


# Create your models here.
class Job(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_id = models.IntegerField(blank=True)
    defunct = models.BooleanField(default=False)

    class Meta:
        app_label = 'job'
        db_table = 'ep_job'
