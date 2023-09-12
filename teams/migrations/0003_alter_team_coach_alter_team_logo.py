# Generated by Django 4.2.4 on 2023-09-10 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_coach_alter_team_motto_team_coach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.coach'),
        ),
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.ImageField(null=True, upload_to='team_logos'),
        ),
    ]