# Generated by Django 2.0.13 on 2019-06-23 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190623_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_width',
        ),
    ]
