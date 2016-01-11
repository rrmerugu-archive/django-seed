__author__ = 'rrmerugu'

from core.models import Post, Category
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return render_to_response('blog/index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()[:5]
    })

def view_post(request, slug):
    return render_to_response('blog/view_post.html', {
        'post': get_object_or_404(Post, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/view_category.html', {
        'category': category,
        'posts': Post.objects.filter(category=category)[:5]
    })