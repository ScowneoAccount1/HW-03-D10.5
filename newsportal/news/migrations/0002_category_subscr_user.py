# Generated by Django 4.1.1 on 2023-01-12 16:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subscr_user',
            field=models.ManyToManyField(related_name='subscribed_categories', to=settings.AUTH_USER_MODEL),
        ),
    ]
