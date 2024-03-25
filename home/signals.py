#import user    
from django.contrib.auth.models import User
from django.db import models
#import profile
from accounts.models import profile
# import signals
from django.db.models.signals import post_save
from django.dispatch import receiver


#when create user then create profile if not exist
@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    user=kwargs["instance"]
    if kwargs["created"]:
        profile.objects.create(user=user)
        