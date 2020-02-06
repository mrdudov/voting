from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

POSIBLE_VOIT = [
    ('plus', 'плюс'),
    ('minus', 'минус'),
    ('none', 'none')
]


class Article(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    text = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    publication_date = models.DateField(blank=True)
    author = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return f'Статья: {self.id}, загаловок: {self.title}'

class News(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    text = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    publication_date = models.DateField(blank=True)
    author = models.ForeignKey('auth.User', related_name='news', on_delete=models.CASCADE)

    def __str__(self):
        return f'Новость: {self.id}, загаловок: {self.title}'


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Vote(models.Model):
    author = models.ForeignKey('auth.User', related_name='votes', on_delete=models.CASCADE)
    vote = models.CharField(choices=POSIBLE_VOIT, blank=True, max_length=100)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = [['author', 'content_type', 'object_id',],]
