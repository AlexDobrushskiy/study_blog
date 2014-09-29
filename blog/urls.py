from django.conf.urls import patterns, include, url
from blog.views import simple_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'application.views.home', name='home'),
    url(r'^/?$', simple_view),
)
