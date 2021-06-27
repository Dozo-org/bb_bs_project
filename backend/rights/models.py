from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag_Right(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Right(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Название'))
    description = models.CharField(max_length=500, verbose_name=_('Описание'))
    text = models.TextField(verbose_name=_('Текст'))
    color = models.CharField(max_length=50, verbose_name=_('Цвет фона'))
    image = models.ImageField(blank=True, verbose_name=_('Изображение'))
    tags = models.ManyToManyField(Tag_Right, verbose_name=_('Теги'))

    def __str__(self):
        return self.title
