from django.db import models

# Create your models here.
class User(models.Model):
    firts_name = models.CharField('Nombre', max_length=15)
    last_name = models.CharField('Apellido', max_length=20)
    user_name = models.CharField('Nombre de usuario', max_length=12, blank=False)
    password = models.IntegerField('Contraseña', blank=False)
    def __str__(self):
        return self.firts_name + " " + self.last_name

class Post(models.Model):
    title = models.CharField('Titulo',max_length=45, blank=False)
    pub_date = models.DateTimeField('Fecha de publicación', blank=False)
    edit_date = models.DateTimeField('Fecha de edición', blank=False)
    content = models.TextField('Contenido', blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Comment(models.Model):
    pub_date = models.DateTimeField('Fecha de publicación', blank=False)
    content = models.TextField('Contenido', blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    entry = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.author + '[' + self.pub_date + ']'

class Tag(models.Model):
    name = models.CharField('Nombre', max_length=12, blank=False)
    entry = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
