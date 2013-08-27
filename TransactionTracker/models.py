import datetime
import django
from django.db import models
from tastypie.utils.timezone import now

# Create your models here.
from django.db.models import Model
from django.contrib.auth.models import User
from django.contrib import admin


class transaction_type(Model):
    description = django.db.models.CharField(max_length=50)
    multiplier = django.db.models.DecimalField(max_digits=12, decimal_places=3)
    owed_multiplier = django.db.models.DecimalField(decimal_places=3, max_digits=12)

    def __str__(self):
        return self.description


class transaction(Model):
    description = django.db.models.CharField(max_length=100)
    date = django.db.models.DateField()
    amount = django.db.models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = django.db.models.ForeignKey(transaction_type)
    user = django.db.models.ForeignKey(User)

    def __unicode__(self):
        return self.description

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = datetime.date.today()

        return super(transaction, self).save(*args, **kwargs)

admin.site.register(transaction_type)