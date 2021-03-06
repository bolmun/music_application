# Generated by Django 2.2.5 on 2020-05-09 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_auto_20200507_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='desired_lesson_days',
            field=models.ManyToManyField(related_name='ads', to='advertisements.LessonDay'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='advertisements.instrumentChoice'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='lesson_type',
            field=models.ManyToManyField(related_name='ads', to='advertisements.LessonType'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='prefer_style',
            field=models.ManyToManyField(related_name='ads', to='advertisements.PreferStyle'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to=settings.AUTH_USER_MODEL),
        ),
    ]
