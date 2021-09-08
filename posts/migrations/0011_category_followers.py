# Generated by Django 3.2.6 on 2021-09-08 11:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0010_remove_category_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='category_followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
