# Generated by Django 4.2.4 on 2023-08-29 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('motto', models.CharField(max_length=64)),
                ('logo', models.ImageField(upload_to='team_logos')),
            ],
        ),
    ]
