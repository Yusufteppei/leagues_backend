# Generated by Django 4.2.4 on 2023-09-12 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_state_useraccount_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='phone',
            field=models.CharField(default=0, max_length=16),
            preserve_default=False,
        ),
    ]
