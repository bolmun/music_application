# Generated by Django 2.2.5 on 2020-05-10 04:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resumes', '0005_auto_20200509_2008'),
        ('reservations', '0002_auto_20200509_2124'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reservtion',
            new_name='Reservation',
        ),
    ]
