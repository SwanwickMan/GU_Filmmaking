# Generated by Django 4.2.11 on 2024-03-21 14:02

import GUFilmmakingApp.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GUFilmmakingApp', '0016_alter_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to=GUFilmmakingApp.models.PathAndRename('thumbnails'), validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
