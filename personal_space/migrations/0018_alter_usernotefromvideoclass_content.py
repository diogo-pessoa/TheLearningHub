# Generated by Django 3.2.6 on 2021-11-22 18:00

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_space', '0017_auto_20211103_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernotefromvideoclass',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
