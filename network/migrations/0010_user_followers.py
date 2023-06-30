# Generated by Django 4.0.6 on 2023-06-04 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_alter_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
