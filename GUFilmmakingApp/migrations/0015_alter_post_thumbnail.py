# Generated by Django 4.2.11 on 2024-03-21 10:21

import GUFilmmakingApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GUFilmmakingApp', '0014_alter_post_file_alter_post_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=GUFilmmakingApp.models.PathAndRename('thumbnails')),
        ),
    ]