from django.db import models
from django.utils import timezone

from django.contrib.gis.db import models

from object.models import Object 

class Waypoint(models.Model):
    name = models.CharField(max_length=32)
    owner = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    lat = models.FloatField()    
    lon = models.FloatField()
    
    object = models.ForeignKey(Object, related_name='waypoint')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return '%s %s %s' % (self.name, self.lat, self.lon)

    class Meta:
        permissions = (
            ("changeown_waypoint", "Can change own waypoint"),
            ("deleteown_waypoint", "Can delete own waypoint"),)