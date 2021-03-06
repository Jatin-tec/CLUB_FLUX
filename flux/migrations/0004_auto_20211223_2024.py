# Generated by Django 3.2.9 on 2021-12-23 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0003_events_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='project category'),
        ),
        migrations.AddField(
            model_name='projects',
            name='start_year',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='project start year'),
        ),
    ]
