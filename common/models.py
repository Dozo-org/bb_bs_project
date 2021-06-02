from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

#User = get_user_model()


# from cities.models import City


class City(models.Model):
    name = models.CharField(max_length=30)
    is_primary = models.BooleanField(default=False)

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
    city = models.ManyToManyField(
        City,
        related_name='users',
        blank=True,
        null=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.is_staff or self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_moderator_reg(self):
        return self.role == 'moderator_reg'

    @property
    def is_mentor(self):
        return self.role == 'mentor'



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name='profile')
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='город', related_name='profile')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'profiles'
        constraints = [
            models.UniqueConstraint(fields=['user', 'city'],
                                    name='unique profile')
            ]