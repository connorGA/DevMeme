# Generated by Django 4.1.3 on 2023-02-17 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_followerscount'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='backgroundimg',
            field=models.ImageField(default='images/resources/timeline-1.jpg', upload_to='background_images'),
        ),
    ]
