from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField('Nombre de usuario', max_length=12, blank=False)
    password = models.IntegerField('Contraseña', blank=False)

class Post(models.Model):
    title = models.CharField('Titulo',max_length=45, blank=False)
    pub_date = models.DateTimeField('Fecha de publicación', blank=False)
    edit_date = models.DateTimeField('Fecha de edición', blank=False)
    content = models.TextField('Contenido', blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    pub_date = models.DateTimeField('Fecha de publicación', blank=False)
    content = models.TextField('Contenido', blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    entry = models.ForeignKey(Post, on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField('Nombre', max_length=12, blank=False)
    entry = models.ForeignKey(Post, on_delete=models.CASCADE)
