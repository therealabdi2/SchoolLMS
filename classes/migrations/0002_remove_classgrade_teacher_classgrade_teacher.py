# Generated by Django 4.1.1 on 2022-09-06 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classgrade',
            name='teacher',
        ),
        migrations.AddField(
            model_name='classgrade',
            name='teacher',
            field=models.ManyToManyField(to='accounts.teacherprofile'),
        ),
    ]
