# Generated by Django 3.0.5 on 2020-06-03 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200601_0416'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='discription',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
