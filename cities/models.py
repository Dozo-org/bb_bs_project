from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class City(models.Model):
    name = models.CharField(max_length=30, verbose_name='имя',)
    is_primary = models.BooleanField(default=False, verbose_name='основной')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name='profile')
    city = models.ManyToManyField(City)

    def __str__(self):
        return self.user.username

