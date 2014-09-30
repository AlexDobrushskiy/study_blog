from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from blog.models import Post
from django.shortcuts import render
from django.views.generic import View


def simple_view(request):
    all_posts = Post.objects.all()

    return HttpResponse(render(request, 'blog/all_records.html', {'posts': all_posts}))


class AddPost(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(render(request, 'blog/add_post.html', {}))

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Post.objects.create(title=title, content=content)

            return HttpResponse('Blog post "%s" succesfully added' % title)
        else:
            return HttpResponseBadRequest('Title and content shoulnd be empty!')