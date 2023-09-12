# Generated by Django 4.2.4 on 2023-09-10 07:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_alter_player_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerrating',
            name='value',
            field=models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AddField(
            model_name='playerrating',
            name='votee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='players.player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playerrating',
            name='voter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='voting_player', to='players.player'),
            preserve_default=False,
        ),
    ]
