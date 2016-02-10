from django.db import models
from django.utils import timezone

from object.models import Object 

class Album(models.Model):
    name = models.CharField(max_length=32)
    owner = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    object = models.ForeignKey(Object, related_name='album')
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    class Meta:
        permissions = (
            ("changeown_album", "Can change own album"),
            ("deleteown_album", "Can delete own album"),)
        
    def __str__(self):
        return '%s' % (self.name)
