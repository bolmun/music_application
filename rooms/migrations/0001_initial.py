# Generated by Django 2.2.5 on 2020-05-13 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Amenities',
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Facilities',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Room Types',
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Rules',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=200)),
                ('price_per_hour', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('is_wind_possible', models.BooleanField(default=False)),
                ('is_percussion_possible', models.BooleanField(default=False)),
                ('all_day', models.BooleanField(default=False)),
                ('instant_book', models.BooleanField(default=False)),
                ('amenities', models.ManyToManyField(blank=True, related_name='rooms', to='rooms.Amenity')),
                ('facilities', models.ManyToManyField(blank=True, related_name='rooms', to='rooms.Facility')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to=settings.AUTH_USER_MODEL)),
                ('room_types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='rooms.RoomType')),
                ('rules', models.ManyToManyField(blank=True, related_name='rooms', to='rooms.Rule')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('caption', models.CharField(max_length=80)),
                ('file', models.ImageField(upload_to='room_photos')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='rooms.Room')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
