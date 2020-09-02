from django.db import models
from django.utils import timezone

# Create your models here.
class Election(models.Model):
    SHIRT_TYPE = (
        ('1', 'Municional'),
        ('2', 'Presidencial')
    )

    name = models.CharField(max_length=200)
    year = models.DateField(auto_now=False, default=timezone.now)
    date_start = models.DateField(auto_now=False, default=timezone.now)
    date_end = models.DateField(auto_now=False, default=timezone.now)

    type_election = models.CharField(max_length=1, default=1, choices=SHIRT_TYPE)

    def __str__(self):
        return str(self.id) + ' - ' +  str(self.name)

    class Meta:
        ordering = ('year', 'name')

    