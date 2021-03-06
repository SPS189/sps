# Generated by Django 3.2.6 on 2022-01-08 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220108_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jobname', models.CharField(max_length=250)),
                ('companyname', models.CharField(max_length=250)),
                ('companyaddress', models.CharField(max_length=250)),
                ('jobdescription', models.CharField(max_length=500)),
                ('qualification', models.CharField(max_length=250)),
                ('responsibilies', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('companywebsite', models.CharField(max_length=250)),
                ('companyemail', models.CharField(max_length=250)),
                ('companycontact', models.CharField(max_length=20)),
                ('salarypackage', models.CharField(max_length=250)),
                ('experience', models.IntegerField()),
            ],
        ),
    ]
