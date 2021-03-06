# Generated by Django 3.2.4 on 2021-06-30 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0004_event_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
        migrations.AlterField(
            model_name='event',
            name='seats',
            field=models.PositiveSmallIntegerField(verbose_name='количество мест'),
        ),
        migrations.AlterField(
            model_name='event',
            name='takenSeats',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='количество занятых мест'),
        ),
    ]
