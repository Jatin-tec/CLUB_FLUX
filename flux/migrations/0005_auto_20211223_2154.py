# Generated by Django 3.2.9 on 2021-12-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0004_auto_20211223_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='projects',
            name='image2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='projects',
            name='image3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='media'),
        ),
    ]
