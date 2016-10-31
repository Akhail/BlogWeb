from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = {'comment_author', 'comment_content'}
		widgets = {
			'comment_author': forms.TextInput({'placeholder': 'Nombre', 'class': 'form-author'}),
			'comment_content': forms.Textarea({'placeholder': 'Comentario', 'class': 'form-content'})
		}
