# Generated by Django 5.0.7 on 2024-08-12 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrymanager', '0011_contestentry_pronouns'),
    ]

    operations = [
        migrations.AddField(
            model_name='hallcontestentry',
            name='pronouns',
            field=models.CharField(default='Unknown', max_length=15),
        ),
    ]
