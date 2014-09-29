from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.shortcuts import render


def simple_view(request):
    all_posts = Post.objects.all()

    return HttpResponse(render(request, 'blog/all_records.html', {'posts': all_posts}))