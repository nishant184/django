# Generated by Django 2.0 on 2020-03-01 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photohireapp', '0002_auto_20200301_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='first', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='second', max_length=200),
        ),
    ]