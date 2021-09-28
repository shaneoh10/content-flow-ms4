# Generated by Django 3.2.6 on 2021-09-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0003_auto_20210920_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('card_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('tokens', models.IntegerField(default=0)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
