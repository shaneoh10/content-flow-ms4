from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="default bio")
    image = models.ImageField(null=True, blank=True,
                              upload_to="profile_images/")

    def __str__(self):
        return self.user.username
