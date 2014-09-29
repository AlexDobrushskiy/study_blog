from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(u'Title', max_length=255)
    content = models.TextField(u'Post content')
    changed = models.DateTimeField(u'Last change date', auto_now=True)

    def __unicode__(self):
        return u'{}. At {}'.format(self.title, self.changed.strftime('%Y-%m-%d %H:%M'))