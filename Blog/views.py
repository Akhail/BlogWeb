import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CommentForm
from .models import Comment, Post


# Create your views here.
def index(request):
	comm = Comment.objects.order_by('-publish_date')[:10]
	post = Post.objects.order_by('-publish_date')[:10]
	return render(request, 'Blog/home.html', {'recent_post': post, 'comments': comm})


def details(request, article=None):
	comm = Comment.objects.order_by('-publish_date')[:10]
	if article is None:
		return render(request, 'Blog/about.html', {'comments': comm})
	
	temp_text = article.replace('-', ' ')
	ps = Post.objects.get(post_title__iexact=temp_text)
	if request.POST:
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.publish_date = datetime.datetime.now()
			comment.post_id = ps
			comment.save()
			return HttpResponseRedirect('/entrada/' + article)
	else:
		form = CommentForm()
	
	comm_post = ps.comment_set.all()
	return render(request, 'Blog/details.html',
	              {'article': ps, 'comments_post': comm_post, 'comments': comm, 'form': form})
