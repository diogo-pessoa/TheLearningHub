# Generated by Django 3.2.6 on 2021-10-17 10:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personal_space', '0004_auto_20211016_2035'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDetail',
            new_name='UserProfile',
        ),
    ]