# Generated by Django 3.2.6 on 2022-01-07 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220107_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='country',
        ),
    ]
