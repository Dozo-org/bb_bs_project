from django.contrib.auth.models import AbstractUser
from django.db import models


class City(models.Model):
    """City models"""

    name = models.CharField(
        max_length=30,
        verbose_name='city'
    )
    is_primary = models.BooleanField(
        verbose_name='Primary City',
        default=False
    )

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


class User(AbstractUser):
    """User augmented fields."""

    class RoleUser(models.TextChoices):
        USER = 'user', 'Пользователь'
        MENTOR = 'mentor', 'Наставник'
        MODERATOR = 'moderator', 'Модератор'
        MODERATOR_REG = 'moderator_reg', 'Модератор региональный'
        ADMIN = 'admin', 'Администратор'

    role = models.CharField(
        verbose_name='role',
        max_length=50,
        blank=True,
        choices=RoleUser.choices,
        default=RoleUser.USER
    )
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True
    )
    city = models.ForeignKey(
        City,
        related_name='users',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.is_staff or self.role == self.RoleUser.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.RoleUser.MODERATOR

    @property
    def is_moderator_reg(self):
        return self.role == self.RoleUser.MODERATOR_REG

    @property
    def is_mentor(self):
        return self.role == self.RoleUser.MENTOR
