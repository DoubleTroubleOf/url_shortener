# Generated by Django 3.0.8 on 2020-07-21 12:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=256, validators=[django.core.validators.URLValidator()])),
                ('url_hash', models.CharField(db_index=True, max_length=10, unique=True)),
                ('short_url', models.CharField(blank=True, max_length=256, null=True, validators=[django.core.validators.URLValidator()])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'URL',
                'verbose_name_plural': 'URLs',
            },
        ),
    ]
