# Generated by Django 3.2.6 on 2021-11-01 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_topic_options'),
        ('personal_space', '0014_rename_body_usernotefromvideoclass_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbookmark',
            name='article',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.article'),
        ),
    ]
