# Generated by Django 3.2.6 on 2021-11-25 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_classes', '0003_alter_videoclass_video_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videoclass',
            old_name='created_at',
            new_name='last_update_at',
        ),
        migrations.RenameField(
            model_name='videoclass',
            old_name='restricted_access',
            new_name='premium_content',
        ),
    ]