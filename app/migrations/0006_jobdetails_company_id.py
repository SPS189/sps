# Generated by Django 3.2.6 on 2022-01-08 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_jobdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetails',
            name='company_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.company'),
            preserve_default=False,
        ),
    ]
