# Generated by Django 4.0.6 on 2023-06-04 02:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_alter_post_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='postLikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
