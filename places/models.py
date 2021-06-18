from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from common.models import City


class PlaceTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Тег')
        verbose_name_plural = _('Теги')

    def __str__(self):
        return self.name


class Place(models.Model):
    class Genders(models.TextChoices):
        MALE = 'M', _('Мальчик')
        FEMALE = 'F', _('Девочка')

    class ActivityTypes(models.IntegerChoices):
        ACTIVE = 0, _('Активный')
        ENTERTAINING = 1, _('Развлекательный')
        INFORMATIVE = 2, _('Познавательный')

    chosen = models.BooleanField(
        verbose_name=_('Выбор наставника'),
        default=False,
    )
    verified = models.BooleanField(
        default=False,
        verbose_name=_('Проверено для публикации'),
    )
    title = models.CharField(
        verbose_name=_('Название'),
        max_length=200,
    )
    address = models.CharField(
        verbose_name=_('Адрес'),
        max_length=200,
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name=_('Город'),
        related_name='places'
    )
    gender = models.CharField(
        verbose_name=_('Пол'),
        choices=Genders.choices,
        max_length=1,
        null=True,
        blank=True,
    )
    age = models.PositiveSmallIntegerField(
        verbose_name=_('Возраст'),
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(25)]
    )
    activity_type = models.PositiveSmallIntegerField(
        verbose_name=_('Тип отдыха'),
        choices=ActivityTypes.choices,
    )
    description = models.TextField(
        verbose_name=_('Комментарий'),
        help_text=_('Поделитесь впечатлениями о проведенном времени'),
    )
    link = models.URLField(
        verbose_name=_('Сайт'),
        help_text=_('Введите адрес сайта'),
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField(PlaceTag, related_name='places', blank=True)
    imageUrl = models.ImageField(
        verbose_name=_('Фото'),
        help_text=_('Добавить фото'),
        null=True,
        blank=True,
        upload_to='places/',
    )
    pubDate = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    class Meta:
        ordering = ('-pubDate',)
        verbose_name = _('Место - куда пойти?')
        verbose_name_plural = _('Места - куда пойти?')

    def __str__(self):
        return self.title

    def list_tags(self):
        return self.tags.values_list('name', flat=True)

    def get_gender(self, gender_code):
        return self.Genders(gender_code).label

    def get_activity_type(self, type_code):
        return self.ActivityTypes(type_code).label
