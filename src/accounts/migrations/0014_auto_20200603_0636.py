# Generated by Django 3.0.5 on 2020-06-03 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_delete_teacherfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='subject',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]