from django.db import models
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = AutoOneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, default="")
    image = models.ImageField(null=True, blank=True, upload_to="profile_images/")
    followers = models.ManyToManyField(User, related_name="user_followers", blank=True)
    tokens_score = models.IntegerField(null=False, blank=False, default=0)
    tokens_balance = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Automatically create user profile or update if created
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
