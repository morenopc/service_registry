from django.db import models


CHANGE_CHOICES = (
    ('created', 'created'),
    ('changed', 'changed'),
    ('removed', 'removed'),
)


class Service(models.Model):
    """Service record"""

    service = models.CharField(max_length=32)
    version = models.CharField(max_length=16)
    change = models.CharField(
        max_length=16, choices=CHANGE_CHOICES, default='created')

    def __str__(self):
        return '%s %s %s' % (self.service, self.version, self.change)
