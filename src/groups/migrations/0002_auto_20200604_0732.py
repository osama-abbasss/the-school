# Generated by Django 3.0.5 on 2020-06-04 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='auther',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_auther', to=settings.AUTH_USER_MODEL),
        ),
    ]
