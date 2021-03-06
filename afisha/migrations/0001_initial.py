# Generated by Django 3.2.4 on 2021-06-06 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, verbose_name='адрес')),
                ('contact', models.CharField(max_length=200, verbose_name='контакт')),
                ('title', models.CharField(max_length=200, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('start_at', models.DateTimeField(verbose_name='начало')),
                ('end_at', models.DateTimeField(verbose_name='окончание')),
                ('seats', models.IntegerField(verbose_name='количество мест')),
                ('taken_seats', models.IntegerField(default=0, verbose_name='количество занятых мест')),
            ],
            options={
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participants', to='afisha.event', verbose_name='мероприятие')),
            ],
            options={
                'verbose_name_plural': 'participates',
            },
        ),
    ]
