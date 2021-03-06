# Generated by Django 3.2.4 on 2021-06-09 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0002_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='event',
            name='unique event',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='end_at',
            new_name='endAt',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='start_at',
            new_name='startAt',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='taken_seats',
            new_name='takenSeats',
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.UniqueConstraint(fields=('city', 'startAt', 'title'), name='unique event'),
        ),
    ]
