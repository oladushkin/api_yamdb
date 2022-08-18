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
