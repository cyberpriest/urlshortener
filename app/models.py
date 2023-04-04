from django.db import models


class URL(models.Model):
    link = models.CharField(max_length=1000)
    uiid = models.CharField(max_length=10)
# Create your models here.
