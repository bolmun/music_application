# Generated by Django 2.2.5 on 2020-05-13 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0006_auto_20200510_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='resumes', to='resumes.instrumentChoice'),
        ),
    ]
