# Generated by Django 3.2.25 on 2024-03-20 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GUFilmmakingApp', '0009_alter_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='hold', unique=True),
            preserve_default=False,
        ),
    ]