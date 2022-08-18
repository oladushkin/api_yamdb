from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Rating(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='review'
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='review'
    )
    score = models.PositiveSmallIntegerField(
        [MaxValueValidator(10)], [MinValueValidator[1]], null=True, blank=True
    )

    def __str__(self):
        return self.score

    class Meta:
        unique_together = ('author', 'scope', 'title')


class Review(models.Model):
    """Модель обзорзоров на произведения"""
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='review'
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='review'
    )
    score = models.ForeignKey(
        Rating, on_delete=models.SET_NULL, related_name='review'
    )


class Comment(models.Model):
    """Модель комментариев к обзорам"""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


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
    name = models.CharField(max_length=50, verbose_name='Название произведения')
    year = models.PositiveSmallIntegerField(
        db_index=True, validators=[MaxValueValidator(date.today().year)],
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