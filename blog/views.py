from django.shortcuts import render,get_object_or_404

# Create your views here.


from django.views import generic
from .models import Post, Category












def blog_posts(request):

	blog_posts = Post.newmanager.all()

	return render(request, 'blog/blog_posts.html', {

			'blog_posts': blog_posts,
		})








def single_post(request, single_post):

	single_post = get_object_or_404(Post, slug=single_post, status='published')

	return render(request, 'blog/single_post.html', {

			'single_post':single_post,
		})










