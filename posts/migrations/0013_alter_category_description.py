# Generated by Django 3.2.6 on 2021-09-10 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0012_category_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.CharField(max_length=255),
        ),
    ]
