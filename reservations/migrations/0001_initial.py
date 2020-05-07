# Generated by Django 2.2.5 on 2020-05-07 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resumes', '0003_photo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservtion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('pending', '예약 내역 확인 중'), ('confirmed', '예약 확정'), ('canceled', '예약 취소')], default='pending', max_length=15)),
                ('meeting_time', models.DateTimeField()),
                ('meeting_address', models.CharField(max_length=200)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumes.Resume')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
