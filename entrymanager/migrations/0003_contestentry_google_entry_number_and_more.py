# Generated by Django 5.0.6 on 2024-07-22 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrymanager', '0002_contestentry_legal_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestentry',
            name='google_entry_number',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='division',
            name='subentry_number',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='contestentry',
            name='judging_time',
            field=models.CharField(choices=[('none', 'Not Assigned'), ('skitonly', 'Skit Entry With No Prejudging'), ('exhibition', 'Strut Your Stuff'), ('072613001400', 'Friday, July 26th, 1pm-2pm'), ('072614001500', 'Friday, July 26th, 2pm-3pm'), ('072615001600', 'Friday, July 26th, 3pm-4pm'), ('072616001700', 'Friday, July 26th, 4pm-5pm'), ('072617001800', 'Friday, July 26th, 5pm-6pm'), ('072710001100', 'Saturday, July 27th, 10am-11am'), ('072711001200', 'Saturday, July 27th, 11am-12pm'), ('072713001400', 'Saturday, July 27th, 1pm-2pm'), ('072714001500', 'Saturday, July 27th, 2pm-3pm')], default='none', max_length=50),
        ),
    ]
