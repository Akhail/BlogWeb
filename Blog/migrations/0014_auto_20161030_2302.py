# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-31 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('Blog', '0013_remove_comment_comment_title'),
	]
	
	operations = [
		migrations.AlterField(
			model_name='comment',
			name='comment_author',
			field=models.CharField(max_length=100, verbose_name='Autor:'),
		),
		migrations.AlterField(
			model_name='comment',
			name='comment_content',
			field=models.TextField(verbose_name='Contenido:'),
		),
	]
