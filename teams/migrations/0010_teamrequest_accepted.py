# Generated by Django 4.2.4 on 2023-09-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0009_teamrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamrequest',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]
