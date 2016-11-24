from ckeditor.fields import RichTextField
from django.db import models
from taggit.managers import TaggableManager


# Create your models here.

class Post(models.Model):
    post_title = models.CharField('Titulo del post', max_length=100, blank=False)
    publish_date = models.DateTimeField('Fecha de publicación', blank=False, auto_now_add=True)
    edit_date = models.DateTimeField('Fecha de edición', blank=False, auto_now=True)
    post_content = RichTextField()
    post_img = models.CharField('Imagen principal', max_length=100, blank=False)
    post_description = models.CharField('Descripción', max_length=500, blank=False)
    post_tags = TaggableManager()

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    comment_author = models.CharField('Autor:', max_length=100, blank=False)
    comment_content = models.TextField('Contenido:', blank=False)
    publish_date = models.DateTimeField('Fecha de publicación', blank=False, auto_now_add=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment_author + ' / ' + self.comment_content[:70]
