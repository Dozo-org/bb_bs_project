from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class City(models.Model):

    name = models.CharField(
        max_length=30,
        verbose_name='city'
    )
    isPrimary = models.BooleanField(
        verbose_name='Primary City',
        default=False
    )

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


class User(AbstractUser):

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
        return self.role == 'mentor'


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Profile'
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        related_name='profiles',
        null=True,
        blank=True,
        verbose_name='City',
        default=False
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ Создаем профиль при создании юзера"""
    if created:
        Profile.objects.create(user=instance, city=instance)
