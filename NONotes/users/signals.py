from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings
from .models import Profile
import os

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # remove all previous profile pics before saving
    path = os.path.dirname(instance.profile.image.path)
    for root, dirs, files  in os.walk(path):
        for file in files:
            if file != os.path.basename(instance.profile.image.path):
                os.remove(os.path.join(root, file))
    
    instance.profile.save()
    
