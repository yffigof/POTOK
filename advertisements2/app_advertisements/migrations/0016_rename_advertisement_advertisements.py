# Generated by Django 4.2.2 on 2023-08-18 15:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_advertisements', '0015_alter_advertisement_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Advertisement',
            new_name='Advertisements',
        ),
    ]
