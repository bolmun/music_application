# Generated by Django 2.2.5 on 2020-05-11 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20200511_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_percussion_possible',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='is_wind_possible',
            field=models.BooleanField(default=False),
        ),
    ]
