from django.db import models

# Create your models here.


class Services(models.Model):
    """
    Services model
    """
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=20, null=False, blank=False)
    service_desc = models.TextField(max_length=255, null=False, blank=False)

    def _str__(self):
        return self.service_name
