# Generated by Django 2.2.5 on 2020-05-07 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='wanna_test_class',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='max_fee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='min_fee',
            field=models.IntegerField(default=0),
        ),
    ]
