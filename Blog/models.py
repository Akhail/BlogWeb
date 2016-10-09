from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    post_title = models.CharField('Titulo del Post',max_length=100, blank=False)
    publish_date = models.DateTimeField('Fecha de publicación', blank=False)
    edit_date = models.DateTimeField('Fecha de edición', blank=False)
    post_content = models.TextField('Contenido', blank=False)
    def __str__(self):
        return self.post_title
    def published(self):
        self.publish_date = timezone.now()
        self.save()

class Comment(models.Model):
    publish_date = models.DateTimeField('Fecha de publicación', blank=False)
    comment_content = models.TextField('Contenido del comentario', blank=False)
    comment_author = models.CharField('Autor del comentario', blank=False)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.author + '[' + self.pub_date + ']'
