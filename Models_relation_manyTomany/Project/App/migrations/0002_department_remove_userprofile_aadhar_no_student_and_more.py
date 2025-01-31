# Generated by Django 5.1.5 on 2025-01-21 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=50)),
                ('dep_des', models.TextField()),
                ('dep_had', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='Aadhar_no',
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=50)),
                ('stu_email', models.EmailField(max_length=254)),
                ('stu_roll', models.CharField(max_length=50)),
                ('stu_dep', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App.department')),
            ],
        ),
        migrations.DeleteModel(
            name='Aadhar',
        ),
        migrations.DeleteModel(
            name='Userprofile',
        ),
    ]
