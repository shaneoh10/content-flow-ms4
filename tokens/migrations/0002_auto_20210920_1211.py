# Generated by Django 3.2.6 on 2021-09-20 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tokens", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="icon_url",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.FloatField(default=0),
        ),
    ]
