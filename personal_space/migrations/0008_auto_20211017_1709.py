# Generated by Django 3.2.6 on 2021-10-17 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal_space', '0007_auto_20211017_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usernote',
            old_name='note_content',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='usernote',
            old_name='note_title',
            new_name='title',
        ),
    ]
