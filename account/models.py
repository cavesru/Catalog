from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver (post_save, sender=User)
def default_group(sender, **kwargs):
    if kwargs.get('created', True):
        user = kwargs.get('instance')
        user.groups.add(Group.objects.get(name='Users'))