# Generated by Django 3.2.6 on 2021-10-16 20:35

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('personal_space', '0003_auto_20211016_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='bookmarks',
        ),
        migrations.AddField(
            model_name='userbookmark',
            name='type',
            field=models.CharField(default='article', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userbookmark',
            name='content_path',
            field=models.CharField(default='/article/8/', max_length=256),
            preserve_default=False,
        ),
    ]
