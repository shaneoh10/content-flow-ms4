from django.db import models
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField


class UserProfile(models.Model):
    user = AutoOneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="default bio")
    image = models.ImageField(null=True, blank=True,
                              upload_to="profile_images/")
    followers = models.ManyToManyField(User, related_name="user_followers",
                                       blank=True)
    tokens_score = models.IntegerField(null=False, blank=False, default=0)
    tokens_balance = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.user.username
