# Generated by Django 2.0.13 on 2019-06-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='posts'),
        ),
    ]
