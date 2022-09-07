# Generated by Django 4.1.1 on 2022-09-06 05:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='class_grades')),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.teacherprofile')),
            ],
        ),
    ]
