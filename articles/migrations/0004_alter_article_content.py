# Generated by Django 3.2.6 on 2021-11-20 19:38

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_topic_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(default='<p></p>', verbose_name='Content'),
            preserve_default=False,
        ),
    ]
