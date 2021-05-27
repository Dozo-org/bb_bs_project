# Generated by Django 3.0.5 on 2021-05-27 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, verbose_name='адрес')),
                ('contact', models.CharField(max_length=200, verbose_name='контакт')),
                ('title', models.CharField(max_length=200, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('start_at', models.DateTimeField(verbose_name='начало')),
                ('end_at', models.DateTimeField(verbose_name='окончание')),
                ('seats', models.IntegerField(verbose_name='количество мест')),
                ('taken_seats', models.IntegerField(default=0, verbose_name='количество занятых мест')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='events', to='cities.City', verbose_name='город')),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participants', to='events.Event', verbose_name='мероприятие')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participates', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name_plural': 'participate',
            },
        ),
        migrations.AddConstraint(
            model_name='eventparticipant',
            constraint=models.UniqueConstraint(fields=('user', 'event'), name='unique participate'),
        ),
    ]
