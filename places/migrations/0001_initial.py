# Generated by Django 3.2.4 on 2021-06-28 09:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0004_alter_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chosen', models.BooleanField(default=False, verbose_name='Выбор наставника')),
                ('verified', models.BooleanField(default=False, verbose_name='Проверено для публикации')),
                ('showOnMain', models.BooleanField(default=True, verbose_name='Показать на главной')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Мальчик'), ('F', 'Девочка')], max_length=1, null=True, verbose_name='Пол')),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(25)], verbose_name='Возраст')),
                ('activity_type', models.PositiveSmallIntegerField(choices=[(0, 'Активный'), (1, 'Развлекательный'), (2, 'Познавательный')], verbose_name='Тип отдыха')),
                ('description', models.TextField(help_text='Поделитесь впечатлениями о проведенном времени', verbose_name='Комментарий')),
                ('link', models.URLField(blank=True, help_text='Введите адрес сайта', null=True, verbose_name='Сайт')),
                ('imageUrl', models.ImageField(blank=True, help_text='Добавить фото', null=True, upload_to='places/', verbose_name='Фото')),
                ('pubDate', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='common.city', verbose_name='Город')),
                ('tags', models.ManyToManyField(blank=True, related_name='places', to='places.PlaceTag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Место - куда пойти?',
                'verbose_name_plural': 'Места - куда пойти?',
                'ordering': ('-pubDate',),
            },
        ),
    ]
