from django.db import models
from django.utils import timezone
import datetime

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_time = models.DateTimeField('event date')
    event_price = models.FloatField('event price')
    event_description = models.CharField(max_length=1000)

    def __str__(self):
        return "%s, %s, %s, %s" % (self.event_name, self.event_time, self.event_price, self.event_description)

    def is_recent_event(self):
        return self.event_time >= timezone.now() - datetime.timedelta(days=1)

