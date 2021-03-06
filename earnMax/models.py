from django.db import models
from django.contrib.postgres.fields import ArrayField
from userlogin.models import UserData

# Create your models here.

class earnMaxData(models.Model):
    emailId = models.EmailField(max_length=100, primary_key=True, default='')
    pile = ArrayField(models.IntegerField())
    scores = ArrayField(models.IntegerField())
    total = models.IntegerField()

    def __str__(self):
        return str(self.email_id)