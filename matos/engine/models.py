from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

@python_2_unicode_compatible
class Operation(models.Model):
    operation = models.CharField(max_length=30)
    numbers = JSONField()
    result = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()

    def __str__(self):
        return "%s (%s): %s" % (self.date, self.ip, self.operation )

    class Meta:
        ordering = ('date',)
