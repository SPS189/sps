# Generated by Django 3.2.6 on 2022-01-07 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='country',
            field=models.CharField(default='India', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='experience',
            field=models.CharField(default='Exp', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='highestedu',
            field=models.CharField(default='PG', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='job_type',
            field=models.CharField(default='Full', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='jobcategory',
            field=models.CharField(default='IT', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='jobdescription',
            field=models.CharField(default='Job Description', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='max_salary',
            field=models.BigIntegerField(default=100000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='min_salary',
            field=models.BigIntegerField(default=50000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='shift',
            field=models.CharField(default='Day', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='website',
            field=models.CharField(default='http://sumit.com', max_length=150),
            preserve_default=False,
        ),
    ]
