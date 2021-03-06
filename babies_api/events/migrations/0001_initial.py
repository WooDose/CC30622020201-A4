# Generated by Django 3.0.4 on 2020-05-01 01:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('babies_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('event_type', models.CharField(default='N/A', max_length=80)),
                ('notes', models.CharField(max_length=800)),
                ('baby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='babies_app.Baby')),
            ],
        ),
    ]
