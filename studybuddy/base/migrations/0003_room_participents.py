# Generated by Django 4.0.2 on 2022-02-13 16:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_room_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='participents',
            field=models.ManyToManyField(blank=True, related_name='participents', to=settings.AUTH_USER_MODEL),
        ),
    ]
