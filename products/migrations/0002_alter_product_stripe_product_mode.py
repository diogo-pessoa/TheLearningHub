# Generated by Django 3.2.6 on 2021-12-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stripe_product_mode',
            field=models.CharField(default='subscription', max_length=100, null=True),
        ),
    ]