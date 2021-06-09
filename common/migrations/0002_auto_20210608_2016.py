# Generated by Django 3.2.4 on 2021-06-08 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles', to='common.city', verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='common.user', verbose_name='Profile'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
