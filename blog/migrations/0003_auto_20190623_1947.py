# Generated by Django 2.0.13 on 2019-06-23 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_height',
            field=models.PositiveIntegerField(blank=True, default='400', editable=False, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image_width',
            field=models.PositiveIntegerField(blank=True, default='600', editable=False, null=True),
        ),
    ]
