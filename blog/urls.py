from django.conf.urls import patterns, include, url
from blog.views import simple_view, AddPost

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'application.views.home', name='home'),
    url(r'^/?$', simple_view),
    url(r'^add/?$', AddPost.as_view()),
)
