# Generated by Django 3.2.4 on 2021-06-28 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_profile_profile value unique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('mentor', 'Наставник'), ('moderator', 'Модератор'), ('moderator_reg', 'Модератор региональный'), ('admin', 'Администратор')], default='mentor', max_length=50, verbose_name='role'),
        ),
    ]
