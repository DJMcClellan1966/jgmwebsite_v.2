from django.shortcuts import render, get_object_or_404

from .models import Blog

def blog(request):
    blogs = Blog.objects
    return render(request, "posts/blog.html", {'blogs': blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'posts/detail.html', {'blog':detailblog})
