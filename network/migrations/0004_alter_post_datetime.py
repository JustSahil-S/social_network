# Generated by Django 4.0.6 on 2023-06-03 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_post_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dateTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
