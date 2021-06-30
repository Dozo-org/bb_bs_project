# Generated by Django 3.2.4 on 2021-06-30 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_tag'),
        ('afisha', '0003_auto_20210609_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='events', to='common.Tag', verbose_name='Теги'),
        ),
    ]