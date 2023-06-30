# Generated by Django 4.0.6 on 2023-06-04 03:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_alter_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='postLikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
