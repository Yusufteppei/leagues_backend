# Generated by Django 4.2.4 on 2023-09-11 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0005_rename_policy_rules_alter_rules_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='rules',
            name='maximum_number_of_players',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rules',
            name='minimum_number_of_players',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]