from datetime import date

from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import CustomUserManager


ROLES = [
    ('user', 'Аутентифицированный пользователь'),
    ('moderator', 'Модератор'), ('admin', 'Администратор'),
    ('superuser', 'Суперюзер Django')
]


class CustomUser(AbstractBaseUser):
    """Кастомная модель пользователя"""
    username = models.CharField(max_length=150, unique=True,
                                validators=[UnicodeUsernameValidator],)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)
    role = models.CharField(
        choices=ROLES, max_length=10, default='user'
    )
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'role']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'


class Category(models.Model):
    """Модель для определения категории."""
    name = models.CharField(max_length=50, verbose_name='Название категории')
    slug = models.SlugField(unique=True, verbose_name='slug')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Модель для определения жанра."""
    name = models.CharField(max_length=50, verbose_name='Название жанра')
    slug = models.SlugField(unique=True, verbose_name='slug')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Title(models.Model):
    """Модель для определения произведений."""
    name = models.CharField(
        max_length=50, verbose_name='Название произведения'
    )
    year = models.PositiveSmallIntegerField(
        db_index=True,
        validators=[
            MaxValueValidator(date.today().year)
        ],
        verbose_name='Год создания произведения'
    )
    description = models.TextField(
        blank=True, max_length=200,
        verbose_name='Описание'
    )
    genre = models.ManyToManyField(
        Genre, related_name='titles',
        blank=True, verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name='titles', blank=True,
        null=True, verbose_name='Категория'
    )

    class Meta:
        ordering = ('year',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name[:15]


class Rating(models.Model):
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='review'
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='review'
    )
    score = models.PositiveSmallIntegerField(
        [MaxValueValidator(10)],
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.score

    class Meta:
        unique_together = ('author', 'score', 'title')


class Review(models.Model):
    """Модель обзорзоров на произведения"""
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='author'
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='title'
    )
    score = models.ForeignKey(
        Rating, on_delete=models.SET_NULL,
        null=True,
    )


class Comment(models.Model):
    """Модель комментариев к обзорам"""
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
