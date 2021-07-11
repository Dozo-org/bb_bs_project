from django.db import models

from common.models import Tag


class Question(models.Model):
    tags = models.ManyToManyField(
        Tag,
        related_name='questions',
        verbose_name='Теги'
    )
    question = models.CharField('Вопрос', max_length=500, unique=True)
    answer = models.TextField('Ответ на вопрос', blank=True, null=True)
    pubDate = models.DateTimeField('Дата публикации', auto_now_add=True)
    chosen = models.BooleanField('Выбор наставника', default=False)

    class Meta:
        ordering = ['pubDate']
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question[:30]

    def list_tags(self):
        return self.tags.values_list('name')
