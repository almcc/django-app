from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from base.models import Profile


@receiver(post_save, sender=User)
def create_user_profile_signal(sender, instance, created, **kwargs):
    """Create a user profile for newly created user."""
    if created:
        Profile.objects.create(user=instance)
