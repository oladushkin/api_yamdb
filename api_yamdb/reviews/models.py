from django.db import models


class Review(models.Model):
    """Модель обзорзоров на произведения"""
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='review')
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='review'
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
