# Generated by Django 4.2.4 on 2023-09-10 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0004_alter_competition_logo_alter_league_logo_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Policy',
            new_name='Rules',
        ),
        migrations.AlterModelOptions(
            name='rules',
            options={'verbose_name_plural': 'Rules'},
        ),
    ]
