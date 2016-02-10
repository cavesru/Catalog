from django.db import models
from django.utils import timezone

class Object (models.Model):
    name = models.CharField (max_length=63)
    owner = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    moderated = models.BooleanField(default=False)
    
    length = models.IntegerField (default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    class Meta:
        permissions = (
            ("changeown_object", "Can change own object"),
            ("deleteown_object", "Can delete own object"),)
    
    def __str__(self):
        return '%s' % (self.name)
    

    

